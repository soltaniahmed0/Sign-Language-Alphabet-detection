from tkinter import filedialog
import customtkinter as ctk

def loadfile():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))
    filenameL.configure(text="File Opened: "+filename)

root=ctk.CTk()
root.geometry(f"{500}x{300}")
frame=ctk.CTkFrame(root,width=200, height=200,corner_radius=10, fg_color="grey")
frame.pack()
loadfilebtn=ctk.CTkButton(frame,text="loadfile",command=loadfile)
loadfilebtn.pack()
filenameL=ctk.CTkLabel(frame,text="")
filenameL.pack()
root.mainloop()