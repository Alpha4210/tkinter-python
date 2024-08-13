# from tkinter import *

# class GUI(Tk):
#     def __init__(self):
#         super().__init__() #Getting everything from the super class
#         self.geometry("744x377") #setting the geomertry of the GUI
#     def status(self):
#         self.var = StringVar()
#         self.var.set("Ready")
#         self.statusbar = Label(self, textvariable=self.var, relief=SUNKEN, anchor=W)
#         self.statusbar.pack(side=BOTTOM, fill=X)
#     def click(self):
#         print("Button clicked")
#     def createbutton(self, inptext):
#         Button(text=inptext, command=self.click).pack()

# if __name__ =='__main__':
#     window = GUI() #Window will be used instead of root
#     window.status()
#     window.createbutton("Yoooooo")
#     window.mainloop() 

#Quick quiz 1 - Create a custom class.

from tkinter import *
root = Tk()
root.geometry("655x444")
root.title("title of my GUI")
root.wm_iconbitmap("download.ico") #Used to set a favicon for the GUI
# root.configure(background="red") #Used to change background of GUI 

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="Close", command=root.destroy).pack() #Used to quit an application

root.mainloop()

# Further code in calculator_project.py



# Videos - 26, 27, 28