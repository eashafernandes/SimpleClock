from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("My Clock")
root.configure(background="black")

def getTime():
    time_value = strftime('%H:%M:%S %p')
    label.config(text = time_value)
    label.after(1000, getTime)

label = Label(root, font = ("Baskerville Old Face", 50), background = "black", foreground = "white")
label.pack(anchor="center", pady= 5, padx= 5)
getTime()

mainloop()