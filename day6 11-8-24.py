from tkinter import *
import tkinter.messagebox as tmsg #Used to display a message box
root = Tk()
root.geometry("733x566")
root.title("ldfjds")

#sample function to test
def myfunc():
    print("YOoo difjadsfsad i")
   
#Function for help 
def myhelp():
    a = tmsg.showinfo("Help", "I will help you with this gui") #Its return value is ok #First argument title, second content

#Function to get rating for our app    
def rate():
    value = tmsg.askquestion("Was your experience good?", "You used this GUI.... was your experience good?") #First argument title, second content
    print(value)
    if value == "yes":
        msg = "Great. Rate us on microsoft store please"
    else:
        msg = "please let us know what went wrong, we will contant you."
    tmsg.showinfo("Experience", msg)    

def abc():
    ans = tmsg.askretrycancel("ABC","wanna be friends with abc")
    if ans:
        print("Retry krne pr kuch nhi hoga")
    else:
        print("kaushfkshf")
#Used to create non drop down menu
# mymenu = Menu(root) #Used to create a menu taskbar
# mymenu.add_command(label="File", command=myfunc) #Add butons to the taskbar
# mymenu.add_command(label="exit", command=quit) #quit is used to exit the gui
# root.config(menu=mymenu) #Packing the menu

#Drop-down menu
mainmenu = Menu(root) #Full menu bar
m1 = Menu(mainmenu, tearoff=0) #First option, tearoff is used to remove the dotted line optio
m1.add_command(label="New Project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_command(label="Save As", command=myfunc)
m1.add_separator() #Used to add a seperator
m1.add_command(label="Print", command=myfunc)
mainmenu.add_cascade(label="File", menu=m1)
root.config(menu=mainmenu)

m2 = Menu(mainmenu, tearoff=0) #First option, tearoff is used to remove the dotted line optio
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_command(label="Paste", command=myfunc)
m2.add_separator() #Used to add a seperator
m2.add_command(label="xyz", command=myfunc)
mainmenu.add_cascade(label="Edit", menu=m2)
root.config(menu=mainmenu)

m3 = Menu(mainmenu, tearoff=0) #First option, tearoff is used to remove the dotted line optio
m3.add_command(label="Help", command=myhelp)
m3.add_command(label="Rate us", command=rate)
m3.add_command(label="Befriend abc", command=abc)
mainmenu.add_cascade(label="Help", menu=m3)
root.config(menu=mainmenu)

root.mainloop()





# Videos - 18, 19