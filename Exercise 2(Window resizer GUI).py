# Create a GUI window that takes the input of width and height
# Create a Button "Apply" and after clicking on this button it will change the size of the GUI window accordingly

from tkinter import *
root = Tk()
root.geometry("655x566")
def inpval():
    root.geometry(f"{a.get()}x{b.get()}")

Label(root, text="Window resizer GUI", font="verdana 19 bold").grid(row=0,column=3)
Label(root, text="Enter height for GUI: ").grid(row=4, column=1)
Label(root, text="Enter width for GUI: ").grid(row=5, column=1)

a = StringVar()
b = StringVar()
i1 = Entry(root, textvariable=b)
i1.grid(row=4, column=2)
i2 = Entry(root, textvariable=a)
i2.grid(row=5, column=2)

Button(root, text="Resize", command=inpval).grid(row=7, column=1, pady=20)
root.mainloop()