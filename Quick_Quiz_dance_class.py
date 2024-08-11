from tkinter import *
root = Tk()
root.geometry("1000x500")

#Text for our form
name = Label(root, text="Name")
email = Label(root, text="Email")
phone = Label(root, text="Phone")
age = Label(root, text="Age")
dance = Label(root, text="Type of dance")

#Packing the text
name.grid(row=1, column=0)
email.grid(row=2, column=0)
phone.grid(row=3, column=0)
age.grid(row=4, column=0)
dance.grid(row=5, column=0)

#Creating input boxes





root.mainloop()