from tkinter import *
from tkinter import ttk

import detailedAboutRenderer

def createWindow():
    #Create window object
    window = Tk()
    window.attributes('-topmost', True)

    #Specify window constraints
    window.config(width="800", height="600", bg="#A9B2AC")
    window.title("The Librarian")
    addwindowElements(window)
    
    #Launch window
    window.mainloop()

def addwindowElements(window):
    #Description text
    aboutText = "The Librarian is a simple, safe, and easy to pick up software designed to make managing files easier. This software allows you to store easy access to any file throughout your system in one area. "
    whyText = "The Librarian allows files in different locations to be accessed easily in one location. This allows you to do multiple things including save space, save time, and prevent the possible dangers when moving files. The Librarian also includes an Undo/Redo functionality to increase workflow and allow the user to prevent possible mistakes."

    #Create window elements
    l1 = Label(window, text="About", font=("Arial", 45))

    l2 = Label(window, text="What is The Librarian?", font=("Arial", 26))
    t1 = Label(window, text=aboutText, font=("Arial", 16), wraplength=600)

    l3 = Label(window, text="Why should you use The Librarian?", font=("Arial", 26))
    t2 = Label(window, text=whyText, font=("Arial", 16), wraplength=600)
    b1 = Button(window, text="Learn More", font=("Arial", 24), command=detailedAboutRenderer.createWindow)

    #Set colors for elements
    l1['bg'] = '#898980'
    l2['bg'] = '#A9B2AC'
    t1['bg'] = '#A9B2AC'
    l3['bg'] = '#A9B2AC'
    t2['bg'] = '#A9B2AC'
    b1['bg'] = '#C5DAC1'


    #Add elements to window
    l1.grid(column=0, row=0, padx=60, pady=15)
    l2.grid(column=0, row=1, padx=60, pady=15)
    t1.grid(column=0, row=2, padx=60, pady=15)
    l3.grid(column=0, row=3, padx=60, pady=15)
    t2.grid(column=0, row=4, padx=60, pady=15)
    b1.grid(column=0, row=5, padx=60, pady=15)