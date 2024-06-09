import time

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.skin = None
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.last_update_time = time.time()

# Ja się tym zajmę - Kasia
    def skin_selection(self):
        print("Wybierz swego zwierzaka:")
        print("""
            1. [;.;] - 
            2. [;.;] - 
            3. [;.;] - 
            4. [;.;] - 
              """)
        choice = None
        while True:
        choice = input ("Którą skórkę wybierasz? [1 - 4]")

# tu jest upływ czasu i wszystko będzie już działało
    def update_status(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_update_time
        
        # Zmniejszanie parametrów w zależności od upływu czasu
        self.hunger -= elapsed_time * 0.5
        self.happiness -= elapsed_time * 0.5
        self.energy -= elapsed_time * 0.5
        
        # Zabezpieczenie przed ujemnymi wartościami
        self.hunger = max(self.hunger, 0)
        self.happiness = max(self.happiness, 0)
        self.energy = max(self.energy, 0)
        
        self.last_update_time = current_time
        

# karmienie, można dodać jakieś różne jedzonka i ile to jedzenie daje
    def feed(self):


# zabawa, można dodać zabawki i ile dana zabawka daje happiness i ile zabiera energy. Można też dodać ile czasu zabiera   
    def play(self):


# sen, można też zabierać czas i hungry  
    def sleep(self):

# tu chyba nic nie trzeba dodawać
    def status(self):
        self.update_status()
        print(f"Status {self.name}: Głód: {self.hunger:.2f}, Szczęście: {self.happiness:.2f}, Energia: {self.energy:.2f}")


# Mogę się tym zająć
def main():
    name = input("Podaj imię swojego Tamagotchi: ")
    pet = Tamagotchi(name)
    skin = pet.skin_selection()

    while True:
        print("\nCo chcesz zrobić?")
        print("1. Nakarm")
        print("2. Pobaw się")
        print("3. Połóż spać")
        print("4. Sprawdź status")
        print("5. Zakończ")
        choice = input("Wybierz opcję: ")

        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.sleep()
        elif choice == '4':
            pet.status()
        elif choice == '5':
            print("Koniec gry. Do zobaczenia!")
            break
        else:
            print("Niepoprawny wybór. Spróbuj ponownie.")

        time.sleep(1)

if __name__ == "__main__":
    main()
