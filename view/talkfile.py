from tkinter import *
import cv2
from PIL import Image, ImageTk
win=Tk()
win.geometry("700x350")
label=Label(win)
label.grid(row=0,column=0)
cap=cv2.VideoCapture(0)


def show_frames():

    label.configure(text="")
    # Repeat after an interval to capture continiously
    label.after(20, show_frames)


show_frames()

win.mainloop()