import tkinter as tk
import pyttsx3

def on_enter(event):
    assistante = pyttsx3.init()
    assistante.say("Button hovered")
    assistante.runAndWait()

root = tk.Tk()
button = tk.Button(root, text="Hover over me")
button.pack()

button.bind("<Enter>", on_enter)

root.mainloop()
