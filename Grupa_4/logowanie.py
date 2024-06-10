import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

root = tk.Tk()
root.geometry("500x400")
root.title("Monitorowanie budżetu")

root.configure(bg="misty rose")

def login():
    name = str(entry_field1.get())
    print("Witaj!" + name)


frame = tk.Frame(bg="misty rose")

title = tk.Label(frame, text="Witaj! Oto twój tracker finansów.", font=("Times New Roman", 20), bg="misty rose", pady=30)
title.grid(column=0, row=0, columnspan=2)

title2 = tk.Label(frame, text="Zaloguj się aby śledzić swoje wydatki", font=("Times New Roman", 25), bg="misty rose", pady=20)
title2.grid(column=0, row=1, columnspan=2)

label1 = tk.Label(frame, text="Twój login:", bg="misty rose", font=("Times New Roman", 10), pady=10)
label1.grid(column=0, row=2)

entry_field1 = tk.Entry(frame)
entry_field1.grid(column=1, row=2)

label2 = tk.Label(frame, text="Podaj hasło:", bg="misty rose", font=("Times New Roman", 10), pady=10)
label2.grid(column=0, row=3)

entry_field2 = tk.Entry(frame, show="*")
entry_field2.grid(column=1, row=3)

button1 = tk.Button(frame, text="Zaloguj się", bg="hot pink", font=("Times New Roman", 10), command=login)
button1.grid(column=0, row=4, columnspan=2)

frame.pack()

class AnimatedGIFLabel(tk.Label):
    def __init__(self, master, path, *args, **kwargs):
        self.master = master
        self.path = path
        self.frames = []
        
        self.load_frames()
    
        super().__init__(master, image=self.frames[0], *args, **kwargs)
        
        self.current_frame = 0
        self.animate()
        
    def load_frames(self):
        with Image.open(self.path) as img:
            for frame in ImageSequence.Iterator(img):
                frame_image = ImageTk.PhotoImage(frame.copy())
                self.frames.append(frame_image)
    
    def animate(self):
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.config(image=self.frames[self.current_frame])
        self.master.after(100, self.animate)  

gif_path = "swinka.gif"

animated_label = AnimatedGIFLabel(root, gif_path)
animated_label.pack(pady=20)


root.mainloop()