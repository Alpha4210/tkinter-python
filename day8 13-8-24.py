from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__() #Getting everything from the super class
        self.geometry("744x377") #setting the geomertry of the GUI
    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvariable=self.var, relief=SUNKEN, anchor=W)
        self.statusbar.pack(side=BOTTOM, fill=X)
    def click(self):
        print("Button clicked")
    def createbutton(self, inptext):
        Button(text=inptext, command=self.click).pack()

if __name__ =='__main__':
    window = GUI() #Window will be used instead of root
    window.status()
    window.createbutton("Yoooooo")
    window.mainloop() 

#Quick quiz 1 - Create a custom class.







# Videos - 26