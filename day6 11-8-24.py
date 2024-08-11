from tkinter import *
root = Tk()
root.geometry("733x566")
root.title("ldfjds")

def myfunc():
    print("YOoo difjadsfsad i")

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
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0) #First option, tearoff is used to remove the dotted line optio
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_command(label="Paste", command=myfunc)
m2.add_separator() #Used to add a seperator
m2.add_command(label="xyz", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

root.mainloop()





# Videos - 18,