import mysql.connector
def connecttoDB():
    try:
        db=mysql.connector.connect(host="localhost",user="root",password="",db="pythonP")
        print("Coonected")
        return db
    except:
        db.rollback()
        print("Error occurred")
