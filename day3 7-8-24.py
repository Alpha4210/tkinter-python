# from tkinter import *

# root = Tk()
# root.geometry("1000x500")
# root.title("GUI") #Used to set title of the gui.

# # Important label options
# # text - adds the text
# # bg - background
# # fg - foreground
# # font - sets the font
# # syntax of font - font=("comicsansms", 19, "bold") or font=("comicsansms 19 bold")
# # padx - padding in X
# # pady - padding in Y
# # relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

# title_label = Label(text='''Blackrocks Brewery is a craft brewery in Marquette, Michigan, United States.\n Taking the name from a local landmark, former pharmaceutical salesmen David Manson and Andy Langlois opened Blackrocks in 2010.\n They originally brewed their products in the basement of a Victorian-style house and used the building's other two floors as a taproom.''', bg='red', fg='white', padx=23, pady=44, font=("comicsansms", 8, "bold"), borderwidth=3, relief=SUNKEN)

# # Important pack options
# # anchor = nw
# # side = top(defualt), bottom, left, right
# # fill = 
# # padx = 
# # pady = 

# title_label.pack(side=BOTTOM, anchor=SW, fill=X)

# root.mainloop()

from tkinter import *

root = Tk()
root.geometry("655x333")
f1 = Frame(root, bg='grey', borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, borderwidth=8, bg='grey', relief=SUNKEN)
f2.pack(side=TOP, fill=X)

l1 = Label(f1, text="Project Tkinter - PyCharm")
l1.pack()

l2 = Label(f2, text="Welcome to Sublime Text", font="Helvetica 16 bold", fg='red')
l2.pack()

root.mainloop()









# #Videos - 7, 8, 9.