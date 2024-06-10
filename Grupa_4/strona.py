import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

root = tk.Tk()
root.geometry("500x400")
root.title("Monitorowanie budżetu")

root.configure(bg="misty rose")



frame = tk.Frame(bg="misty rose")

title = tk.Label(frame, text="Witaj ponownie.", font=("Times New Roman", 20), bg="misty rose", pady=30)
title.grid(column=0, row=0)

title2 = tk.Label(frame, text="Oto Twoje ostatnie transakcje:", font=("Times New Roman", 20), bg="misty rose", pady=20)
title2.grid(column=0, row=1)

###### tutaj powinna być tabela z wydatkami

label1 = tk.Label(frame, text="Śledź swoje wpływy i wydatki ", bg="misty rose", font=("Times New Roman", 15), pady=10)
label1.grid(column=7, row=1)

def roczne_wydatki():
    ###### tutaj powinien byc wykres

btn = tk.Button(frame, text ='Zobacz swoje wydatki roczne', command = roczne_wydatki, pady=10)
btn.grid(column=7, row=2)

def miesieczne_wydatki():
     ###### tutaj powinien byc wykres

btn = tk.Button(frame, text ='Zobacz swoje miesięczne wydatki', command = miesieczne_wydatki, pady=10)
btn.grid(column=7, row=5)

frame.pack()

root.mainloop()
