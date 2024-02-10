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
    l1 = Label(window, text="Create Section", font=("Arial", 60))
    l2 = Label(window, text="Name: ", font=("Arial", 32))
    e1 = Entry(window, font=("Arial", 32), width=15)

    #Set colors for elements
    l1['bg'] = '#898980'
    l2['bg'] = '#C5DAC1'
    e1['bg'] = '#C5DAC1'

    #Add elements to window
    l1.grid(column=0, row=0, padx=60, pady=15)
    l2.grid(column=0, row=1, pady=0)
    e1.grid(column=0, row=2, pady=0)

createWindow()