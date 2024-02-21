from tkinter import *
from tkinter import ttk

import helpAdvancedRenderer

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
    openText = "To open a desired file, either double click it in the file viewer or click the 'Open' button after clicking on the file."
    addText = "To add a file to your current section first click 'Add File'. After File Explorer has opened, navigate to your desired file to add, click on the file and click Open. The file will then be added to your current section."
    removeText = "To remove a file from your current section click on a file in the file viewer. Make sure to only do a single click or it will open the file. After clicking on the file click 'Remove File' and the file will be removed from your current section."
    undoredoText = "If you accidently make a mistake and wish to undo your action simply click 'Undo' and the software will handle it for you. If you need to redo an undo simply click 'Redo' and the undo will be reverted."

    #Create window elements
    l1 = Label(window, text="Help", font=("Arial", 45))

    l2 = Label(window, text="How do I open a file?", font=("Arial", 26))
    t1 = Label(window, text=openText, font=("Arial", 16), wraplength=600)

    l3 = Label(window, text="How do I add a file?", font=("Arial", 26))
    t2 = Label(window, text=addText, font=("Arial", 16), wraplength=600)

    l4 = Label(window, text="How do I remove a file?", font=("Arial", 26))
    t3 = Label(window, text=addText, font=("Arial", 16), wraplength=600)

    l5 = Label(window, text="How to Undo or Redo?", font=("Arial", 26))
    t4 = Label(window, text=undoredoText, font=("Arial", 16), wraplength=600)

    l6 = Label(window, text="Need more?", font=("Arial", 26))
    b1 = Button(window, text="View advanced", font=("Arial", 16), command=helpAdvancedRenderer.createWindow)

    #Set colors for elements
    l1['bg'] = '#898980'
    l2['bg'] = '#A9B2AC'
    t1['bg'] = '#A9B2AC'
    l3['bg'] = '#A9B2AC'
    t2['bg'] = '#A9B2AC'
    l4['bg'] = '#A9B2AC'
    t3['bg'] = '#A9B2AC'
    l5['bg'] = '#A9B2AC'
    t4['bg'] = '#A9B2AC'
    l6['bg'] = '#A9B2AC'
    b1['bg'] = '#C5DAC1'


    #Add elements to window
    l1.grid(column=0, row=0, padx=60, pady=15)
    l2.grid(column=0, row=1, padx=60, pady=15)
    t1.grid(column=0, row=2, padx=60, pady=0)
    l3.grid(column=0, row=3, padx=60, pady=15)
    t2.grid(column=0, row=4, padx=60, pady=0)
    l4.grid(column=0, row=5, padx=60, pady=15)
    t3.grid(column=0, row=6, padx=60, pady=0)
    l5.grid(column=0, row=7, padx=60, pady=15)
    t4.grid(column=0, row=8, padx=60, pady=0)
    l6.grid(column=0, row=9, padx=60, pady=0)
    b1.grid(column=0, row=10, padx=60, pady=0)
