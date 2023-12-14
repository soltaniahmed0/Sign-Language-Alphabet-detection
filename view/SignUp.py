from tkinter import messagebox
import customtkinter
import mysql.connector
from DBConnection import *
from DAO_users import *
def singuser(Username,password,name,Disability,tabview):
    if (len(Username) ==0  or len(password) ==0 or len(name) ==0 ):
        print("fill up the form please")
        messagebox.showwarning("fill the form","Fill up the form please")
    else:
        u=fetch_User(Username)
        if u==Username:
            messagebox.showwarning("Exist","User already Exist")
            print("User already Exist")
        else:
            InsertUser(Username,password,Disability,name)
            messagebox.showinfo("User Added", "User is added")
            tabview.set("Login")