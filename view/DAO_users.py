from DBConnection import *

def fectch_Userby(Username,Password):
    con = connecttoDB()
    cursor = con.cursor()
    Query = "Select username ,password from users where username=%s and password =%s"
    values=(Username,Password)
    cursor.execute(Query,values)
    rows = cursor.fetchall()
    u=" fsdf"
    for row in rows:
        u = row[0]
        print(u)
    return u
def fetch_User(Username):
    con = connecttoDB()
    cursor = con.cursor()
    Query = "Select username from users where username='" + Username + "'"
    cursor.execute(Query)
    u=""
    rows = cursor.fetchall()
    for row in rows:
        u = row[0]
    return u
def InsertUser(Username,Password,Disability,name):
    con=connecttoDB()
    cursor=con.cursor()
    Query="Insert into users values (%s,%s,%s,%s)"
    value=(Username,Password,Disability,name)
    cursor.execute(Query,value)
    cursor.execute("commit")
    print("user added")
def getName(Username,Password):
    con = connecttoDB()
    cursor = con.cursor()
    Query = "Select name from users where username=%s and password =%s"
    values=(Username,Password)
    cursor.execute(Query,values)
    rows = cursor.fetchall()
    u=" fsdf"
    for row in rows:
        u = row[0]
        print(u)
    return u
def getDisability(Username,Password):
    con = connecttoDB()
    cursor = con.cursor()
    Query = "Select Disability from users where username=%s and password =%s"
    values=(Username,Password)
    cursor.execute(Query,values)
    rows = cursor.fetchall()
    u=" fsdf"
    for row in rows:
        u = row[0]
        print(u)
    return u
