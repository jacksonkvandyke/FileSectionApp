from tkinter import *
from tkinter import ttk

from tkinter import messagebox

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
    openText = 'There are a couple reasons as to why section may not be opening, follow these troubleshooting steps:'
    bulletOne = '• Check the JSON file syntax'
    bulletTwo = '• Check your JSON files section'
    bulletThree = '• Restart the software'

    manualText = "If you wish to add files to your section manually you can, start by opening your section JSON file as a text document. Then find the files:{} section within the JSON object and add a file:{} object. After doing this, add a filename and filepath attribute to the object and your file should show in your section. If it does not appear, use the 'Check Correct Syntax' button to ensure you have set it up correctly."

    #Create window elements
    l1 = Label(window, text="Advanced Help", font=("Arial", 45))

    l2 = Label(window, text="Section won't open?", font=("Arial", 26))
    t1 = Label(window, text=openText, font=("Arial", 16), wraplength=600)

    t2 = Label(window, text=bulletOne, font=("Arial", 16), wraplength=600)
    b1 = Button(window, text="Check", font=("Arial", 10), command=lambda: messagebox.showinfo("The Librarian", 'Correct Syntax:\n\n{"isfilesortFile": "true", "filename": "Your Section Name", "files": {}}', parent=window))

    t3 = Label(window, text=bulletTwo, font=("Arial", 16), wraplength=600)
    b2 = Button(window, text="Check", font=("Arial", 10), command=lambda: messagebox.showinfo("The Librarian", 'File Syntax:\n\n{"filename": Your File Name, "filepath": Your File Path}', parent=window))

    t4 = Label(window, text=bulletThree, font=("Arial", 16), wraplength=600)

    l3 = Label(window, text="How to manually add files", font=("Arial", 26))
    t5 = Label(window, text=manualText, font=("Arial", 16), wraplength=600)
    b3 = Button(window, text="Check Correct Syntax", font=("Arial", 10), command=lambda: messagebox.showinfo("The Librarian", 'File Syntax:\n\n{"filename": Your File Name, "filepath": Your File Path}', parent=window))


    #Set colors for elements
    l1['bg'] = '#898980'
    l2['bg'] = '#A9B2AC'
    t1['bg'] = '#A9B2AC'
    t2['bg'] = '#A9B2AC'
    b1['bg'] = '#C5DAC1'
    t3['bg'] = '#A9B2AC'
    b2['bg'] = '#C5DAC1'
    t4['bg'] = '#A9B2AC'
    l3['bg'] = '#A9B2AC' 
    t5['bg'] = '#A9B2AC'
    b3['bg'] = '#C5DAC1'
    


    #Add elements to window
    l1.grid(column=0, row=0, padx=60, pady=15)
    l2.grid(column=0, row=1, padx=60, pady=15)
    t1.grid(column=0, row=2, padx=60, pady=5, sticky='w')
    t2.grid(column=0, row=3, padx=60, pady=5, sticky='w')
    b1.grid(column=0, row=4, padx=60, pady=0)
    t3.grid(column=0, row=5, padx=60, pady=5, sticky='w')
    b2.grid(column=0, row=6, padx=60, pady=0)
    t4.grid(column=0, row=7, padx=60, pady=5, sticky='w')
    l3.grid(column=0, row=8, padx=60, pady=5)
    t5.grid(column=0, row=9, padx=60, pady=5)
    b3.grid(column=0, row=10, padx=60, pady=0)