import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#wczytanie pliku z transakcjami
data = pd.read_csv('testowe_transakcje.csv')
df = pd.DataFrame(data)

#sortowanie całej df po dacie
df.sort_values(by=['Data'], inplace=True)
#konwersja na typ data
data['Data'] = pd.to_datetime(data['Data'])
#stworzenie mini df pokazujacej tylko wydatki
c1 = df[df["Typ Transakcji"]=="Wydatek"]
#stworzenie mini df pokazującej tylko Wpływy
c2 = df[df["Typ Transakcji"]=="Wpływ"]
#sumowanie wydatków i wpływów w poszczególnych kategoriach
data['Data'] = pd.to_datetime(data['Data'])
suma_wydatkow_kategoria = c1.groupby('Kategoria').sum()['Kwota'].reset_index()
suma_wplywow_kategoria = c2.groupby('Kategoria').sum()['Kwota'].reset_index()
#tworzenie wykresu #1
bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']
plt.figure(figsize=(10, 6))
plt.bar(suma_wydatkow_kategoria['Kategoria'], suma_wydatkow_kategoria['Kwota'], color=bar_colors,)
plt.xlabel('Kategoria')
plt.ylabel('Kwota')
plt.title('Suma wydatków w poszczegolnych kategoriach ')
plt.savefig('Wykres_suma_wydatków_kategoria.png')
#nowy data frame do liniowego z ujemnymi
data['Data'] = pd.to_datetime(data['Data'])
do_liniowego = c1.groupby(['Kategoria', 'Data']).sum()['Kwota'].reset_index()
do_liniowego.sort_values(by=['Data'], inplace=True)
#nowy data frame do liniowego bez ujemnych
data['Data'] = pd.to_datetime(data['Data'])
do_liniowego_2 = c1.groupby(['Kategoria', 'Data']).sum()['Kwota'].reset_index()
do_liniowego_2.sort_values(by=['Data'], inplace=True)
do_liniowego_2

#Tworzenie wykresu #2
plt.figure(figsize=(12, 8))
do_liniowego['Kwota'][2] = -180
#print(do_liniowego['Sumaryczny'])

do_liniowego['Sumaryczny'] = do_liniowego['Kwota'].cumsum() ## Sumaryczny budzet
## Sumaryczny jest plotowany pierwszy, bo obejmuje caly zakres dat
plt.plot(do_liniowego.sort_values(by='Data')['Data'], do_liniowego.sort_values(by='Data')['Sumaryczny'], color="red", linewidth=2.5)


# Przechodzenie przez kategorie
for kategoria in do_liniowego['Kategoria'].unique():
    # Wybranie danych dla danej kategorii
    dane_kategorii = do_liniowego[do_liniowego['Kategoria'] == kategoria]

    # Tworzenie wykresów
    ## dodanie wykresu punktowego, bo dla jednego punktu nie zostanie stworzony wykres liniowy
    ## a to pomineloby kategorie Rozrywka w tej sytuacji
    plt.plot(dane_kategorii['Data'], dane_kategorii['Kwota'], label=kategoria, marker='o')
    ## Poniewaz mamy juz legende z polecenia powyzej, tutaj ja "wylaczamy" przez label='_nolegend'
    plt.plot(dane_kategorii['Data'], dane_kategorii['Kwota'], label='_nolegend_')


plt.title('Zmiana wydatków przeznaczonych na poszczególne kategorie w czasie')
plt.xlabel('Data')
plt.ylabel('Kwota')
plt.legend()
plt.show()
#Wykres numer #3
do_liniowego_2['Data'] = pd.to_datetime(do_liniowego_2['Data'])
wydatki_miesiac_kategoria = do_liniowego_2.groupby([do_liniowego_2['Data'].dt.strftime('%Y-%m'), 'Kategoria'])['Kwota'].sum().unstack()
wydatki_miesiac_kategoria.plot(kind='bar', figsize=(12, 8))
plt.title('Wydatki w poszczególnych kategoriach w każdym miesiącu')
plt.xlabel('Miesiąc')
plt.ylabel('Kwota')
plt.savefig('Wykres_wydatki_w_miesiącu.png')
#nowy df do wykresu kołowego #4
do_kolowego = do_liniowego_2.groupby('Kategoria')['Kwota'].sum()
# Tworzenie wykresu kołowego
plt.figure(figsize=(8, 8))
plt.pie(do_kolowego, labels=do_kolowego.index, autopct='%1.1f%%')
plt.title('Wydatki na poszczególne kategorie w całym roku')
plt.savefig('Wydatki_kolowy_calyrok.png')

#znowu kazało przekształcić
do_liniowego['Data'] = pd.to_datetime(do_liniowego_2['Data'])

# Pobranie daty od użytkownika
rok = input("Podaj rok dla którego chcesz zobaczyć dane (np. 2023): ")
czy_sam_rok = input("Czy chcesz zobaczyć dane z konkretnego miesiąca Y/N?: ")

if czy_sam_rok.lower() in ['n', 'no']:
    wybrany_rok = f"{rok}"
    dane_wybranego_roku = do_liniowego_2[do_liniowego_2['Data'].dt.strftime('%Y') == wybrany_rok]

    # Sprawdzenie, czy dane dla wybranego roku istnieją
    if dane_wybranego_roku.size == 0:
        print(f"Brak danych dla wybranego roku: {wybrany_rok}")
    else:
        suma_wydatkow_kategorie = dane_wybranego_roku.groupby('Kategoria')['Kwota'].sum()

        # Tworzenie wykresu #5
        plt.figure(figsize=(8, 8))
        plt.pie(suma_wydatkow_kategorie, labels=suma_wydatkow_kategorie.index, autopct='%1.1f%%')
        plt.title(f'Wydatki na poszczególne kategorie w roku {wybrany_rok}')
        plt.savefig('Wydatki_rok_userdefined.png')
else:
    miesiac = input("Podaj miesiąc (np. 01 dla Styczeń): ")
    wybrany_rok_miesiac = f"{rok}-{miesiac}"
    dane_wybranego_rok_miesiac = do_liniowego[do_liniowego['Data'].dt.strftime('%Y-%m') == wybrany_rok_miesiac]

    # Sprawdzenie, czy dane dla wybranego miesiąca i roku istnieją
    if dane_wybranego_rok_miesiac.size == 0:
        print(f"Brak danych dla wybranego miesiąca i roku: {wybrany_rok_miesiac}")
    else:
        suma_wydatkow_kategorie = dane_wybranego_rok_miesiac.groupby('Kategoria')['Kwota'].sum()

        # Tworzenie wykresu kołowego #6
        plt.figure(figsize=(8, 8))
        plt.pie(suma_wydatkow_kategorie, labels=suma_wydatkow_kategorie.index, autopct='%1.1f%%')
        plt.title(f'Wydatki na poszczególne kategorie w {wybrany_rok_miesiac}')
        plt.savefig('Wydatki_rokmiesiac_userdefined.png')

#utworzone kategorie oraz ich słowa klucz
kategorie = {
    'dom': ['rachunki','podatki','czynsz','remont','naprawy'],
    'transport': ['paliwo','bilet','taxi','ubezpieczenie','mechanik','eksploatacja'],
    'rozrywka': ['kino','teatr','muzeum','restauracja','basen','wakacje','subskrypcja','hobby'],
    'zdrowie': ['lekarstwa','lekarz','badanie'],
    'usługi': ['fryzjer','kosmetyczka','telefon','internet'],
    'jedzenie': ['jedzenie', 'przekąski', 'dostawa']
}

#komenda która przypisuje wydatki do odpowiedniej kategorii na podstawie jego opisu
def przypisz_kategorie(opis_wydatku, kategorie):
    for kategoria, slowo_klucz in kategorie.items():
        if any(slowo in opis_wydatku.lower() for slowo in slowo_klucz):
            return kategoria
    return 'inne'
    
#sprawdzanie czy został przekroczony limit od 122 do do 185

#komenda, która czyta plik csv z opisanymi wydatkami, które mają zostać skategoryzowane
def czytaj_i_sortuj_csv(plik):
    df = pd.read_csv(plik, encoding='utf-8')
    df['Kategoria'] = df['Opis'].apply(lambda x: przypisz_kategorie(x, kategorie))
    print(df[['Opis','Kategoria']])
    df.to_csv('posortowane_transakcje.csv', index=False)    #nowy plik z dodanymi kategoriami

# Wczytanie pliku z transakcjami
def czytaj_i_sortuj_csv(plik):
    df = pd.read_csv(plik, encoding='utf-8')
    df['Data'] = pd.to_datetime(df['Data'])
    df['Kategoria'] = df['Opis'].apply(lambda x: przypisz_kategorie(x, kategorie))
    return df

# Funkcja do obliczenia wydatków w danym miesiącu dla danej kategorii
def calculate_monthly_expenses(df, year, month, category):
    monthly_expenses = df[(df['Data'].dt.year == year) & (df['Data'].dt.month == month) & (df['Typ Transakcji'] == 'Wydatek')]
    if category != 'Wszystkie':
        monthly_expenses = monthly_expenses[monthly_expenses['Kategoria'] == category]
    total_expenses = monthly_expenses['Kwota'].sum()
    return total_expenses

# Funkcja do sprawdzenia, czy wydatki przekroczyły limit dla każdego miesiąca
def check_budget_limit_for_year(file_path, year, limit, category):
    df = czytaj_i_sortuj_csv(file_path)
    
    for month in range(1, 13):
        total_expenses = calculate_monthly_expenses(df, year, month, category)
        if total_expenses > limit:
            print(f"Alert: Wydatki w miesiącu {month}/{year} dla kategorii '{category}' przekroczyły zadany limit! Suma wydatków: {total_expenses} zł")
        else:
            print(f"Wydatki w miesiącu {month}/{year} dla kategorii '{category}' są w ramach limitu. Suma wydatków: {total_expenses} zł")

# Funkcja do pobrania unikalnych kategorii z pliku CSV
def get_unique_categories(file_path):
    df = czytaj_i_sortuj_csv(file_path)
    categories = df['Kategoria'].unique().tolist()
    categories.append('Wszystkie')
    return categories

# Funkcja pytająca użytkownika o limit i kategorię
def get_user_input(file_path):
    year = int(input("Podaj rok (YYYY): "))
    limit = float(input("Podaj limit wydatków (zł): "))
    categories = get_unique_categories(file_path)
    
    print("Dostępne kategorie: ")
    for category in categories:
        print(f"- {category}")
    
    category = input("Podaj kategorię: ")
    while category not in categories:
        print("Błędna kategoria. Spróbuj ponownie.")
        category = input("Podaj kategorię: ")
    
    return year, limit, category

# Ścieżka do pliku CSV (dostosuj zgodnie z lokalizacją pliku)
file_path = 'testowe_transakcje.csv'  # Przykładowa ścieżka, dostosuj zgodnie z lokalizacją pliku

# Pobranie danych od użytkownika
year, limit, category = get_user_input(file_path)

# Sprawdzenie wydatków dla każdego miesiąca w roku
check_budget_limit_for_year(file_path, year, limit, category)

plik = r''    #plik czytany
czytaj_i_sortuj_csv(plik)
