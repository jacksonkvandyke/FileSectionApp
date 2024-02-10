from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
import subprocess
import os

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
    #Create string variable to update UI
    fileName = StringVar(window)
    chosenDirectory = StringVar(window, "No Directory Selected")
    debugText = StringVar(window)

    #Create window elements
    l1 = Label(window, text="Create Section", font=("Arial", 60))
    l2 = Label(window, text="Name: ", font=("Arial", 32))
    e1 = Entry(window, font=("Arial", 32), textvariable=fileName, width=15)
    b1 = Button(window, text="Choose Location", font=("Arial", 16), command=lambda: openExplorer(window, chosenDirectory), width=15)
    l3 = Label(window, textvariable=chosenDirectory, font=("Arial", 16))
    b2 = Button(window, text="Create Section", font=("Arial", 16), command=lambda: createSection(fileName, chosenDirectory, l4, debugText), width=15)
    l4 = Label(window, textvariable=debugText, font=("Arial", 16))

    #Set colors for elements
    l1['bg'] = '#898980'
    l2['bg'] = '#C5DAC1'
    e1['bg'] = '#C5DAC1'
    b1['bg'] = '#C5DAC1'
    l3['bg'] = '#A9B2AC'
    b2['bg'] = '#C5DAC1'
    l4['bg'] = '#A9B2AC'

    #Add elements to window
    l1.grid(column=0, row=0, padx=60, pady=15)
    l2.grid(column=0, row=1, pady=0)
    e1.grid(column=0, row=2, pady=0)
    b1.grid(column=0, row=3, pady=15)
    l3.grid(column=0, row=4, pady=0)
    b2.grid(column=0, row=5, pady=15)

def openExplorer(window, chosenDirectory):
    window.attributes('-topmost', False)
    #Open file explorer
    userDirectory = askdirectory()
    window.attributes('-topmost', True)

    #Check if user input was empty
    if userDirectory != '':
        chosenDirectory.set(userDirectory)

def createSection(fileName, chosenDirectory, debugLabel, debugText):
    if ((os.path.isdir(chosenDirectory.get()) == False) or (len(fileName.get()) == 0)):
        debugLabel.grid(column=0, row=6)
        debugText.set("Please enter a file name and ensure your chosen directory is valid.")
        return

    try:
        fullName = chosenDirectory.get() + '/' + fileName.get() + '.json'
        newFile = open(fullName, 'w+')
        newFile.write('{"isfilesortFile": "true", "filename": "%s"}' % (fileName.get()))
        debugLabel.grid(column=0, row=6)
        debugText.set("Section successfully created")
    except:
        debugLabel.grid(column=0, row=6)
        debugText.set("Section creation was unsuccessful. Please check your permissions.")