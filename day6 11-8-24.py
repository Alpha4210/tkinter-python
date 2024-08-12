# from tkinter import *
# import tkinter.messagebox as tmsg #Used to display a message box
# root = Tk()
# root.geometry("733x566")
# root.title("ldfjds")

# #sample function to test
# def myfunc():
#     print("YOoo difjadsfsad i")
   
# #Function for help 
# def myhelp():
#     a = tmsg.showinfo("Help", "I will help you with this gui") #Its return value is ok #First argument title, second content

# #Function to get rating for our app    
# def rate():
#     value = tmsg.askquestion("Was your experience good?", "You used this GUI.... was your experience good?") #First argument title, second content
#     print(value)
#     if value == "yes":
#         msg = "Great. Rate us on microsoft store please"
#     else:
#         msg = "please let us know what went wrong, we will contant you."
#     tmsg.showinfo("Experience", msg)    

# def abc():
#     ans = tmsg.askretrycancel("ABC","wanna be friends with abc")
#     if ans:
#         print("Retry krne pr kuch nhi hoga")
#     else:
#         print("kaushfkshf")
# #Used to create non drop down menu
# # mymenu = Menu(root) #Used to create a menu taskbar
# # mymenu.add_command(label="File", command=myfunc) #Add butons to the taskbar
# # mymenu.add_command(label="exit", command=quit) #quit is used to exit the gui
# # root.config(menu=mymenu) #Packing the menu

# #Drop-down menu
# mainmenu = Menu(root) #Full menu bar
# m1 = Menu(mainmenu, tearoff=0) #First option, tearoff is used to remove the dotted line optio
# m1.add_command(label="New Project", command=myfunc)
# m1.add_command(label="Save", command=myfunc)
# m1.add_command(label="Save As", command=myfunc)
# m1.add_separator() #Used to add a seperator
# m1.add_command(label="Print", command=myfunc)
# mainmenu.add_cascade(label="File", menu=m1)
# root.config(menu=mainmenu)

# m2 = Menu(mainmenu, tearoff=0) #First option, tearoff is used to remove the dotted line optio
# m2.add_command(label="Cut", command=myfunc)
# m2.add_command(label="Copy", command=myfunc)
# m2.add_command(label="Paste", command=myfunc)
# m2.add_separator() #Used to add a seperator
# m2.add_command(label="xyz", command=myfunc)
# mainmenu.add_cascade(label="Edit", menu=m2)
# root.config(menu=mainmenu)

# m3 = Menu(mainmenu, tearoff=0) #First option, tearoff is used to remove the dotted line optio
# m3.add_command(label="Help", command=myhelp)
# m3.add_command(label="Rate us", command=rate)
# m3.add_command(label="Befriend abc", command=abc)
# mainmenu.add_cascade(label="Help", menu=m3)
# root.config(menu=mainmenu)

# root.mainloop()

# from tkinter import *
# import tkinter.messagebox as tmsg
# root = Tk()
# root.geometry("455x233")
# root.title("Sliders in tkinter")

# def get_money():
#     print(f"we have credited {myslider2.get()} dollars to your account") #used to get the value of the slider
#     tmsg.showinfo("Money credited",f"we have credited {myslider2.get()} dollars to your account")
# # myslider = Scale(root, from_=0, to=455) #Used to make a vertical slider(number)
# # myslider.pack()
# Label(root, text="How much money do you want?").pack()
# myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=10) #Used to make a horizontal slider(number)
# myslider2.set(32) #Used to set a default value for the slider
# myslider2.pack()

# Button(root, text="Get money!", pady=10, command=get_money).pack()


# root.mainloop()
#quiz -  Make a slider to get customer experience and write it in a file(0 - 10) with the name of person and display a thank you message.
from tkinter import *
import tkinter.messagebox as tmg
def ty():
    print(reviewentry.get())
    if reviewentry.get()<5:
        tmg.showinfo("thank you",f"Thank you {nameval.get()} for the review, please let us know if we can make any improvements. Our email - xyz@gmail.com")
    else:
        tmg.showinfo("thank you",f"Thank you {nameval.get()} for the review, we are glad to know that you liked our food!")
root = Tk()
root.geometry("350x333")
root.title("Food review")

Label(root, text="Review for food", font="verdana 20 bold").grid(row=0, column=1)
Label(root, text="Name", font="comicsansms 10", padx=20).grid(row=1, column=0, pady=15)
Label(root, text="Rating", font="comicsansms 10", padx=20).grid(row=2, column=0, pady=5)

nameval = StringVar()

nameentry = Entry(root,  textvariable=nameval)
nameentry.grid(row=1, column=1)
reviewentry = Scale(root, from_=0, to=10, orient=HORIZONTAL, tickinterval=1, length=150)
reviewentry.set(5)
reviewentry.grid(row=2, column=1)

Button(text="Submit", command=ty).grid(row=4, column=1, pady=30)

root.mainloop()

# # Videos - 18, 19, 20