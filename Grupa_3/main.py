import time

class Tamagotchi:
    def __init__(self, name,skin):
        self.name = name
        self.skin = skin
        self.hunger = 70
        self.happiness = 70
        self.energy = 70
        self.last_update_time = time.time()

    def update_status(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_update_time
        
        # zmniejszanie parametrów w zależności od upływu czasu
        self.hunger -= elapsed_time * 0.3
        self.happiness -= elapsed_time * 0.3
        self.energy -= elapsed_time * 0.3
        
        # zabezpieczenie przed ujemnymi wartościami
        self.hunger = max(self.hunger, 0)
        self.happiness = max(self.happiness, 0)
        self.energy = max(self.energy, 0)

        self.last_update_time = current_time
        
    def feed(self):
        self.update_status()
        food_items = {
            '1': ('Banan', 10),
            '2': ('Jabłko', 10),
            '3': ('Hamburger', 20),
            '4': ('Sałatka', 15),
            '5': ('Winogrono', 10),
            '6': ('Sushi',25)
        }
        
        print("Co chcesz dać do jedzenia?")
        for key, (food, value) in food_items.items():
            print(f"{key}. {food}")

        choice = input("Wybierz jedzenie: ")
        if choice in food_items:
            food, value = food_items[choice]
            self.hunger += value
            self.hunger = min(self.hunger, 100)
            print(f"{self.name} zjadł {food}. Poziom głodu wynosi {self.hunger:.1f}.")
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

    def play(self):
        self.update_status()
        toys = {
                '1':('ball', 10, 5, 2),
                '2':('teddy bear', 15, 8, 3),
                '3':('robot', 20, 7, 4),
            }
        print("Czym chcesz się pobawić?")
        for key, (toy, fun, energy, hunger) in toys.items():
            print(f"{key}. {toy}")

        choice = input("Wybierz zabawkę: ")
        if choice in toys:
            toy, fun, energy, hunger = toys[choice]
            self.happiness += fun
            self.energy -= energy
            self.hunger -= hunger
            self.happiness = min(self.hunger, 100)
            self.energy = max(self.energy, 0)
            self.hunger = max(self.hunger, 0)
            print(f"{self.name} pobawił się {toy}. Poziom radości wynosi {self.happiness:.1f}.")
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")
            
    def sleep(self):
        self.update_status()
        while self.energy < 100:
            self.energy += 10
            self.hunger -= 5
            print(f"{self.name} śpi. Energia: {self.energy:.1f}, Głód: {self.hunger:.1f}")
            time.sleep(3)  # tu można w sekundach ustawić ile będzie spał
            if self.hunger <= 20:
                self.hunger = 20
                print(f"{self.name} jest bardzo głodny i musi się obudzić.")
                break
    
    def status(self):
        self.update_status()
        print(f"Status {self.name}: Głód: {self.hunger:.1f}, Szczęście: {self.happiness:.1f}, Energia: {self.energy:.1f}")

def main():
    def animal_name():
        while True:
            name = input("Podaj imię swojego Tamagotchi: ").strip() #wczytuje imię zwierzęcia od użytkownika i usuwa wszelkie wiodące i końcowe białe znaki za pomocą strip().
            if name.isalpha() and len(name) > 0: # sprawdza, czy imię zawiera tylko litery (alfabetyczne) i ma długość większą niż 0
                print(f"Jego imię to: {name}")
                return name
            else:
                print("Błąd: Imię musi zawierać przynajmniej jedną literę i nie może być pustym łańcuchem. Spróbuj ponownie.")

    def skin_selection():
        print("Wybierz swego zwierzaka:")
        # https://happyafterblog.blogspot.com/2012/08/zwierzatka-na-klawiaturze-ascii.html?fbclid=IwZXh0bgNhZW0CMTAAAR1avKOH-s-Yhd78nZhBHLjqx4w3ua-uQtw3lvGm90MJ_HEDwaxd8rbSZKo_aem_AecjQzrJSzuJbmIHISDX6eflVqHWETK72gMcYUQrP6cm4LpY2ikqDNaWb4_nO8JPTBNGu_ZqeXM5nWYGJ2-mPHgB
        print(""" 
        1. PAPUGA
        2. GĄSKA
        3. ŚWINKA
        4. WIEWIÓRKA
        """)
        choice = None
        while True:
            choice = input ("Którą skórkę wybierasz? [1 - 4]")
            if choice == '1':
                skin =  """
     ______ __
   {-_-_= '. `'.
    {=_=_-  \   |
     {_-_   |   /
      '-.   |  /    .===,
   .--.__\  |_(_,==`  ( o)'-.
  `---.=_ `     ;      `/    |
      `,-_       ;    .'--') /
        {=_       ;=~`    `"`
         `//__,-=~`
         <<__ \\__
         /`)))/`)))"""
                print (f"Wybrałeś papugę: \n{skin}")
                return skin
            elif choice == '2':
                skin = """
                        __
                      /` ,\__
                     |    ).-'
                    / .--'
                   / /
     ,      _.==''`  |
   .'(  _.='         |
  {   ``  _.='       |
   {    \`     ;    /
    `.   `'=..'  .='
      `=._    .='
        '-`\\`__
            `-._{"""
                print (f"Wybrałeś gąske: \n{skin}")
                return skin
            elif choice == '3':
                skin = """
            (\____/)
            / @__@ |
           (  (oo)  )
            `-.~~.-'
             /    |
           @/      \_
          (/ /    \ \)
           WW`----'WW """
                print (f"Wybrałeś świnkę: \n{skin}")
                return skin
            elif choice == '4':
                skin = """
         _.-'''-,
       .'  ..::. `|
      /  .::' `'` /
     / .::' .--.=;
     | ::' /  C ..|
     | :: |   \  _.)
      \ ':|   /  |
       '-, \./ \)\)
          `-|   );/
             '--'-"""
                print (f"Wybrałeś wiewiórkę: \n{skin}")
                return skin
            else:
                print("Niepoprawny wybór. Spróbuj ponownie.")

    name = animal_name()
    skin = skin_selection()
    pet = Tamagotchi(name, skin)
    
    while True:
        print("\nCo chcesz zrobić?")
        print("1. Nakarm")
        print("2. Pobaw się")
        print("3. Połóż spać")
        print("4. Sprawdź status")
        print("5. Zakończ")
        if pet.hunger < 20 and pet.hunger >= 0 or pet.happiness < 20 and pet.happiness >= 0 or pet.energy < 20 and pet.energy >= 0:
            print (skin)
            print ("Jestem nieszczęśliwy :<")
            pet.status()
        elif pet.hunger <= 0 or pet.happiness <= 0 or pet.energy <= 0:
            print (f"\nZabiłeś {pet.name} [*]")
            print("Koniec gry. Następnym razem postaraj się nie zabić swego zwierzaka")
            break
        else:
            print ("\n")

        choice = input("Wybierz opcję: ")
        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.sleep()
        elif choice == '4':
            print (skin)
            pet.status()
        elif choice == '5':
            print("Koniec gry. Do zobaczenia!")
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

        time.sleep(1)

if __name__ == "__main__":
    main()
