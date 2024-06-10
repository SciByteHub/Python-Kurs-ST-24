import time

class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.skin = None
        self.hunger = 70
        self.happiness = 70
        self.energy = 70
        self.last_update_time = time.time()

# upływ czasu - Kasia
    def update_status(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_update_time
        
        # zmniejszanie parametrów w zależności od upływu czasu
        self.hunger -= elapsed_time * 0.5
        self.happiness -= elapsed_time * 0.5
        self.energy -= elapsed_time * 0.5
        
        # zabezpieczenie przed ujemnymi wartościami
        self.hunger = max(self.hunger, 0)
        self.happiness = max(self.happiness, 0)
        self.energy = max(self.energy, 0)

        self.last_update_time = current_time
        
# karmienie ~Honorata
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

# zabawa, można dodać zabawki i ile dana zabawka daje happiness i ile zabiera energy. Można też dodać ile czasu zabiera 
#Ja to zrobię- Sandra
    def play(self):
        if self.energy >= toy.energy_cost
            self.happiness += toy.happiness_boost
            self.energy -= toy.energy_cost
            if self.happiness < 100:
            self.happiness += 10
            print(f"{self.name} pobawił się {toy.name}. Poziom szczęścia wynosi teraz {self.hapiness}")
        else:
            print(f"{self.name} jest już bardzo szczęśliwy.")
class Toy:
    def __init__(self_name, happiness_boost, energy_cost, play_time):
        self.name = name
        self.happiness_boost = happiness_boost
        self.energy_cost = energy_cost
        self.play_time = play_time

def create_toys():
    return [
        Toy('ball', 10, 5, 2),
        Toy('teddy bear', 15, 10, 3),
        Toy('robot', 20, 15, 4),
    ]


# sen, można też zabierać czas i hungry  
    def sleep(self):
        self.update_status()
        while self.energy < 100:
            self.energy += 10
            self.hunger += 5
            print(f"{self.name} śpi. Energia: {self.energy}, Głód: {self.hunger}")
            time.sleep(3)  # tu można w sekundach ustawić ile będzie spał
            if self.hunger >= 100:
                self.hunger = 100
                print(f"{self.name} jest bardzo głodny i musi się obudzić.")
                break
        else:
            print(f"{self.name} jest wypoczęty.")

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
