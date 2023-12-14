from tkinter import filedialog
import customtkinter as ctk
import os

import pyttsx3

from pdfToVoice import readFile

root=ctk.CTk()
def on_enter1(e):
    assistante = pyttsx3.init()
    assistante.say("log file")
    assistante.runAndWait()
def on_enter2(e):
    assistante = pyttsx3.init()
    assistante.say("English")
    assistante.runAndWait()
def on_enter3(e):
    assistante = pyttsx3.init()
    assistante.say("read file")
    assistante.runAndWait()
def on_enter4(e):
    assistante = pyttsx3.init()
    assistante.say("Alphabitecs")
    assistante.runAndWait()
def on_enter5(e):
    assistante = pyttsx3.init()
    assistante.say("Words")
    assistante.runAndWait()
def on_enter6(e):
    assistante = pyttsx3.init()
    assistante.say("Talk time")
    assistante.runAndWait()

def on_enter7(e):
    assistante = pyttsx3.init()
    assistante.say("logout")
    assistante.runAndWait()
def run_camera():
    os.system('python camerafile2.py')
def cameratime():
    os.system('python camerafile.py')
def talkTime():

    os.system('python ../voiceTOText.py')



def logout():
    root.destroy()
    os.system('python main.py')
def startNew(name,disability):
    def run_programm():
        languages = ["English", "Italien", "German", "Spanich", "Russian"]
        for i in range(len(languages)):
            if languages[i] == select_language.get():
                n = i
        n += 1
        TextPath = loadfilebtn.cget("text")
        readFile(TextPath, n)

    def loadfile():
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("Text files",
                                                          "*.pdf*"),
                                                         ("all files",
                                                          "*.*")))
        loadfilebtn.configure(text=filename)
    root.title("Welcome ")
    root.geometry("600x410")
    bigframe=ctk.CTkFrame(master=root, width=200, height=200, corner_radius=10, fg_color="#00204a")
    bigframe.pack(padx=20, pady=20)
    title = ctk.CTkLabel(bigframe, text="Welcome " + name, font=("cursive",30))
    title.pack(pady=10)
    #frame1

    frame = ctk.CTkFrame(master=bigframe, width=180, height=200, corner_radius=10, fg_color="#005792")
    frame.pack( padx=30,pady=20)

    frame.grid_columnconfigure((0,1,2),weight=1)
    #frame1 body

    loadfilebtn = ctk.CTkButton(frame, text="load file", command=loadfile,hover="enable")
    loadfilebtn.grid(row=1,column=0,padx=20,pady=10)
    if(disability=="blind"):

        loadfilebtn.bind("<Enter>",on_enter1)
    select_language = ctk.CTkOptionMenu(frame, values=["English", "Italien", "German", "Spanich", "Russian"])
    select_language.grid(row=1,column=1)
    if (disability == "blind"):

        select_language.bind("<Enter>", on_enter2)
    readbtn=ctk.CTkButton(frame,text="read file",command=run_programm,hover="enable")
    readbtn.grid(row=1,column=2,padx=20)
    if (disability == "blind"):

        readbtn.bind("<Enter>", on_enter3)

    #frame2

    frame2=ctk.CTkFrame(master=bigframe, width=200, height=200, corner_radius=10, fg_color="#005792")
    frame2.pack(pady=20,padx=20)

    frame.grid_columnconfigure((0,1,2), weight=1)
    # frame2 body
    camerabtn=ctk.CTkButton(frame2,text="Alphabetics",command=cameratime,hover="enable")
    camerabtn.grid(row=0,column=0,padx=20,pady=10)
    if (disability == "blind"):

        camerabtn.bind("<Enter>", on_enter4)
    camerabtn2=ctk.CTkButton(frame2,text="Words",command=run_camera,hover="enable")
    camerabtn2.grid(row=0,column=1)
    if (disability == "blind"):

        camerabtn2.bind("<Enter>", on_enter5)
    talkbtn=ctk.CTkButton(frame2, text="talk time", command=talkTime,hover="enable")
    talkbtn.grid(row=0,column=2,padx=20)
    if (disability == "blind"):

        talkbtn.bind("<Enter>", on_enter6)

    # frame3
    frame3=ctk.CTkFrame(master=bigframe, width=200, height=200, corner_radius=30, fg_color="#005792")
    frame3.pack(padx=20, pady=20)
    # frame3 body
    logbtn = ctk.CTkButton(frame3, command=logout, text="logout",hover="enable")
    logbtn.pack()
    if (disability == "blind"):

        logbtn.bind("<Enter>", on_enter7)
    root.mainloop(padx=20, pady=20)
