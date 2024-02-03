from tkinter import *
from tkinter import ttk

def createWindow():
    #Create window object
    window = Tk()

    #Specify window constraints
    window.config(width="800", height="600", bg="#A9B2AC")
    window.title("The Librarian")

    frame = Frame(window)
    addwindowElements(window)
    
    #Launch window
    window.mainloop()

def addwindowElements(window):
    #Create window elements
    l1 = Label(window, text="The Librarian", font=("Arial", 60))
    b1 = Button(window, text="Create Section", font=("Arial", 32), width=15)
    b2 = Button(window, text="Load Section", font=("Arial", 32), width=15)
    b3 = Button(window, text="Settings", font=("Arial", 32), width=15)

    #Set colors for elements
    l1['bg'] = '#898980'
    b1['bg'] = '#C5DAC1'
    b2['bg'] = '#C5DAC1'
    b3['bg'] = '#C5DAC1'

    #Add elements to window
    l1.grid(column=0, row=0, padx=60)
    b1.grid(column=0, row=1, pady=15)
    b2.grid(column=0, row=2, pady=15)
    b3.grid(column=0, row=3, pady=15)

createWindow()