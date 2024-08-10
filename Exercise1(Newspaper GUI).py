#n png files and n txt files, make a newspaper out of it using tkinter
 
from tkinter import *
import os

root = Tk()
root.geometry("1920x1080")
for filename in os.listdir():  
    if filename.endswith('.png'):
        print(filename)
        photo = PhotoImage(file=filename)
        l1 = Label(image=photo)
        l1.pack()
    if filename.endswith('txt'):
        l2 = Label(text='abc')
        l2.pack()

root.mainloop()