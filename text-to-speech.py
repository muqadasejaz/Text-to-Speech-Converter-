import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import os
import pyttsx3
import pygame
import gtts as gTTS


root = Tk()
root.title("Text to Speech Converter")
root.geometry("1000x580+200+80")
root.resizable(False,False)
root.configure(bg="#F7AC40")


tts=pyttsx3.init()
def speak_now():
    text = text_box.get(1.0, END).strip()
    gender = gender_box.get()
    speed = speed_box.get()

    if not text:
        return

    # Destroy old engine and reinitialize fresh
    tts = pyttsx3.init(driverName='sapi5')
    voices = tts.getProperty('voices')

    # Force select correct voice
    if gender == 'Male':
        tts.setProperty('voice', voices[0].id)   # Microsoft David
    else:
        tts.setProperty('voice', voices[1].id)   # Microsoft Zira

    # Adjust speaking rate
    if speed == 'Fast':
        tts.setProperty('rate', 250)
    elif speed == 'Normal':
        tts.setProperty('rate', 150)
    else:
        tts.setProperty('rate', 60)

    # Speak and shut down engine
    tts.say(text)
    tts.runAndWait()
    tts.stop()
    del tts   # make sure engine is destroyed


    
logo_image= PhotoImage(file=r"E:\Muqadas\university\projects\ML\Text-to-Speech Converter\logo3.png")
root.iconphoto(False, logo_image)
# root.mainloop()

upper_frame=Frame(root, bg="#14A7DD", width=1200, height=190)
upper_frame.place(x=0,y=0)

picture= PhotoImage(file=r"E:\Muqadas\university\projects\ML\Text-to-Speech Converter\logo4.png")
Label(upper_frame, image=picture, bg="#14A7DD").place(x=150,y=5)
# root.mainloop()

Label(upper_frame, text="Text to Speech Converter", font="TimesNewroman 40 bold", bg="#14A7DD", fg='white').place(x=340, y=60)
# root.mainloop()

text_box=Text(root, font="Arial 20", bg="white", relief=GROOVE, fg="black", wrap=WORD, bd=0)
text_box.place(x=10, y=200, width=980, height=180)
# root.mainloop()

gender_box=Combobox(root, values=['Male' , 'Female'], font="Arial 14", state='r', width=10)
gender_box.place(x=250, y=400)
gender_box.set('Male')
# root.mainloop()

speed_box=Combobox(root, values=['Fast' , 'Normal', 'Slow'], font="Arial 14", state='r', width=10)
speed_box.place(x=650, y=400)       
speed_box.set('Normal')
# root.mainloop()

Label(root, text="Select Voice", font="Arial 14", bg="#F7AC40", fg="black").place(x=100, y=400)
Label(root, text="Select Speed", font="Arial 14", bg="#F7AC40", fg="black").place(x=500, y=400)
# root.mainloop()

play_button=PhotoImage(file=r"E:\Muqadas\university\projects\ML\Text-to-Speech Converter\play1.png")
# play_butt= Button(root, text='Play',  image=play_button, bg= "#F7AC40", font= 'arial 14 bold', borderwidth='0.1c',  activebackground="#F7AC40", bd=0, cursor="hand2")
# play_butt.place(x=420, y=450)
play_butt = Button(
    root,
    text='Play',
    image=play_button,
    compound='bottom',  # Show text over image
    bg="#F7AC40",
    font='arial 14 bold',
    borderwidth='0.1c',
    activebackground="#F7AC40",
    bd=0,
    cursor="hand2",
    command=speak_now  # Link the button to the speak_now function
)
play_butt.place(x=420, y=450)
root.mainloop()