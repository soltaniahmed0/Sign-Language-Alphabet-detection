from tkinter import messagebox
import customtkinter
import mysql.connector
from DBConnection import *
from DAO_users import *
def GetUser(Username,Password):
    if(len(Username)==0  or len(Password)==0 ):
        messagebox.showinfo("Fill the Form","Fill up the Form please")
    else:
        u=fectch_Userby(Username,Password)
        if u==Username:
           return True
        else:
            messagebox.showwarning("Check", "Check your inforamtion please")
            return False

