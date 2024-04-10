"""
Zadanie 2a

Zainicjalizuj zmienną str_num1 i nadaj jej wartość „16”, następnie zainicjalizuj
zmienną str_num2 i nadaj jej wartość „70”. Stwórz zmienną „I_know_that” i
przypisz do niej działanie dodawania na wcześniej zainicjalizowanych
zmiennych. Następnie użyj funkcji print dla zmiennej „I_know_that”.

"""
"""Definiuję zmienne"""
str_num1 = "16"
str_num2 = "70"

I_know_that = str_num1 + str_num2 # dodaję do siebie utworzone zmienne typu str
print(I_know_that) # W terminalu wyświetla się 1670, bo dodajemy do siebie ciąg znaków, a nie liczby, tzw. konkatenacja