# from tkinter import *
# import tkinter.messagebox as tmsg
# root = Tk()
# root.geometry("455x233")
# root.title("Radiobutton")
# def order():
#     tmsg.showinfo("Order recieved", f"We have recieved your order for {var.get()}. thanks for ordering")
# var = IntVar()
# # var.set(1) #used to set a value to a variable.
# Label(root, text="What would you like to have?", justify=LEFT, padx=14, font="lucida 19 bold").pack()

# radio = Radiobutton(root, text="Dosa", padx=14, variable=var, value=1).pack(anchor=W) #Used to create a radio button
# radio = Radiobutton(root, text="Idli", padx=14, variable=var, value=2).pack(anchor=W)
# radio = Radiobutton(root, text="Paratha", padx=14, variable=var, value=3).pack(anchor=W)
# radio = Radiobutton(root, text="Samosa", padx=14, variable=var, value=4).pack(anchor=W)

# #Small task 1 - Try to create these radiobutton using for loop

# Button(text="order now", command=order).pack()

# root.mainloop()

# from tkinter import *
# root = Tk()
# root.geometry("455x233")
# root.title("Listbox")

# def add():
#     global i
#     listbox.insert(ACTIVE, f"{i}") #Active will insert the element above the selected element.
#     i+=1
# i=0
# lbx = Listbox(root) # Used to create a list box
# lbx.pack()
# lbx.insert(END, "First item of our list box") #Used to insert items in the listbox

# Button(root, text="Add item", command=add).pack()

# root.mainloop()







#  Videos - 21, 22