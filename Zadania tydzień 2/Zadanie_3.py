"""
Zadanie 3
Wyobraź sobie, że dopiero zaczynasz cykl edukacji. Jesteś uczniem pierwszej klasy
szkoły podstawowej. Jedynymi przedmiotami, jakie masz w szkole są: język polski,
matematyka oraz religia.

a) Stwórz listę „subjects” i przypisz do niej jako osobne elementy przedmioty jakie
masz w szkole. Wypisz listę za pomocą „print”.
"""

subjects = ["język polski", "matematyka", "religia"] # tworzę listę z przedmiotami szkolnymi
print(subjects) # wypisuję listę w terminalu za pomocą funkcji "print"

"""
b) Czas szybko mija, jesteś już w czwartej klasie, pojawiają się nowe przedmioty:
angielski oraz przyroda. Stwórz listę „new_subjects” i przypisz do niej nowe
przedmioty. Następnie dodaj do listy „subjects” listę „new_subjects”. Wypisz listę
za pomocą „print”
"""

new_subjects = ["angielski", "przyroda"]
subjects = subjects + new_subjects # dodaję do pierwotnej listy nowe przedmioty
print(subjects) # wypisuję listę w terminalu za pomocą funkcji "print"

"""
c) Polityka jest nieprzewidywalna. Polska została najechana przez Indonezję,
wskutek czego język polski w szkołach zastąpiony zostaje językiem
indonezyjskim. Dostosuj swoją listę do warunków politycznych. Wypisz listę za
pomocą „print”
"""
subjects[0] = "język indonezyjski" # zastępuję język polski (o indeksie 0, bo jest na pierwszym miejscu w liście) na liście językiem indonezyjskim
print(subjects) # wypisuję listę w terminalu za pomocą funkcji "print"

"""
d) Chciałbyś wiedzieć ilu przedmiotów uczysz się w szkole, jednak nauczycielka
matematyki zna się na wszystkim, tylko nie na przedmiocie, którego naucza.
Użyj odpowiedniej funkcji, aby dowiedzieć się, ile masz przedmiotów. Wynik
działania tej funkcji wypisz za pomocą funkcji „print”.
"""

liczba_przedmiotow = len(subjects) # za pomocą funkcji len uzyskuję liczbę elementów listy i przypisuję tę wartość do zmiennej "liczba_przedmiotów"
print(liczba_przedmiotow) # wypisuję w terminalu liczbę przedmiotów

"""
e) Wszystko co dobre kiedyś się kończy, wraz z nadejściem 6 klasy kończy się Twoja
edukacja religijna. Usuń religię z listy. Wypisz listę za pomocą „print”.
"""

del subjects[2] # usuwam z listy element o indeksie 2 pod którym w tym przypadku kryje się religia
"""
wersja alternatywna rozwiązania
usuniety_przedmiot = subjects.remove("religia")
"""
print(subjects) # wypisuję listę w terminalu za pomocą funkcji "print"

"""
f) Zostałeś wyrzucony ze szkoły za nielegalny handel batonikami i nazwanie
nauczycielki przyrody „tyranozaurem”. Wyczyść swoją listę, nie będzie Ci już
potrzebna. Wypisz listę za pomocą „print”.
"""

subjects.clear() # używam funkcji clear, aby wyczyścić listę
print(subjects) # wypisuję listę w terminalu za pomocą funkcji "print"