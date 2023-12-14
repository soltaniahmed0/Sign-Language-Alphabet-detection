import speech_recognition as sr
import customtkinter as ctk

root = ctk.CTk()

def cancel():
    root.destroy()

def Cont():
    root.destroy()

def recognize_voice():
    UserVoiceRecognizer = sr.Recognizer()
    try:
        with sr.Microphone() as UserVoiceInputSource:
            UserVoiceRecognizer.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.5)
            UserVoiceInput = UserVoiceRecognizer.listen(UserVoiceInputSource)
            UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput)
            UserVoiceInput_converted_to_Text = UserVoiceInput_converted_to_Text.lower()
            readtext.configure(text=UserVoiceInput_converted_to_Text)
            print(UserVoiceInput_converted_to_Text)
    except sr.UnknownValueError:
        print("No User Voice detected or unintelligible noises detected")

root.geometry("500x300")
frame = ctk.CTkFrame(master=root, width=200, height=200, corner_radius=10, fg_color="grey")
frame.pack(padx=20, pady=20)
readtext = ctk.CTkLabel(frame, text="", font=("cursive", 30))
readtext.pack(padx=20, pady=20)
frame2 = ctk.CTkFrame(master=root, width=200, height=200, corner_radius=10, fg_color="grey")
frame2.pack(padx=20, pady=20)
btn1 = ctk.CTkButton(frame2, text="Quit", command=cancel)
btn1.grid(row=0, column=0, padx=20, pady=20)
btn2 = ctk.CTkButton(frame2, text="Continue", command=Cont)
btn2.grid(row=0, column=1, padx=20, pady=20)
btn_listen = ctk.CTkButton(frame2, text="Listen", command=recognize_voice)
btn_listen.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

root.mainloop()
