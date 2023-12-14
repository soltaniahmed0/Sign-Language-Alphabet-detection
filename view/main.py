from tkinter import messagebox
import customtkinter as ctk
import cv2
import pyttsx3

from SignUp import *
from Login import *
from DAO_users import *

from StartActivity import *
ctk.set_appearance_mode("dark")
root=customtkinter.CTk()
root.geometry("840x610")
root.title("SignHelper")

def log():
    if(GetUser(UsernameE.get(),PasswordE.get())):
        name=getName(UsernameE.get(),PasswordE.get())
        disability=getDisability(UsernameE.get(),PasswordE.get())
        print(disability)
        root.destroy()
        startNew(name,disability)



def signup():
    singuser(UsernameES.get(),PasswordES.get(),NameES.get(),selectDisability.get(),tabview)

frame=ctk.CTkFrame(master=root,width=200,height=200,corner_radius=10,fg_color="grey")
frame.pack(padx=20, pady=20)

title=ctk.CTkLabel(frame,text="SignHelper")
title.pack(pady=3)
tabview=ctk.CTkTabview(frame)
tabview.add("Login")
tabview.add("Sign up")
tabview.set("Login")
tabview.pack(padx=10,pady=2,expand=True)
#Login
def on_enter(e):
    assistante = pyttsx3.init()
    assistante.say("login")
    assistante.runAndWait()

userL=ctk.CTkLabel(tabview.tab("Login"),text="Username")
userL.pack(pady=5)
UsernameE=ctk.CTkEntry(tabview.tab("Login"))
UsernameE.pack()
passL=ctk.CTkLabel(tabview.tab("Login"),text="Password")
passL.pack(pady=5)
PasswordE=ctk.CTkEntry(tabview.tab("Login"),show="*")
PasswordE.pack()
login=ctk.CTkButton(tabview.tab("Login"),text="Log in",command=log,hover="enable")
login.bind('<Enter>',on_enter)
login.pack(pady=10)


#Sign Up
def on_enter_sign(e):
    assistante = pyttsx3.init()
    assistante.say("Signup")
    assistante.runAndWait()
NameSL=ctk.CTkLabel(tabview.tab("Sign up"),text="Name")
NameSL.pack(pady=5)
NameES=ctk.CTkEntry(tabview.tab("Sign up"))
NameES.pack()
UsernameLS=ctk.CTkLabel(tabview.tab("Sign up"),text="Username")
UsernameLS.pack()
UsernameES=ctk.CTkEntry(tabview.tab("Sign up"))
UsernameES.pack()
passLS=ctk.CTkLabel(tabview.tab("Sign up"),text="Password")
passLS.pack(pady=5)
PasswordES=ctk.CTkEntry(tabview.tab("Sign up"),show="*")
PasswordES.pack()
firstoption=ctk.StringVar(value="mute")
selectDisability=ctk.CTkOptionMenu(tabview.tab("Sign up"),values=["mute","deaf","blind","normal"],variable=firstoption)
Disability = selectDisability.get()
selectDisability.pack(pady=5)
singUp=ctk.CTkButton(tabview.tab("Sign up"),text="Sign up",command=signup,hover="enable")
singUp.pack(pady=10)
singUp.bind("<Enter>",on_enter_sign)



root.mainloop()
