from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text") #this function is used to get the value of the button
    if text=="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get()) #Eval evaluates a string
            
            except Exception as e:
                print(e)
                value = "Error"
        
        
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text) #Used to show the value of the screen of calculator
        screen.update() 

root = Tk()
root.geometry("644x900")
root.wm_iconbitmap("download.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucia 40 bold")
screen.pack(fill=X, padx=10, pady=10, ipadx=8)

f = Frame(root, bg="grey")
f.pack()

b = Button(f, text="9", font="lucida 35 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", font="lucida 35 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", font="lucida 35 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()

b = Button(f, text="6", font="lucida 35 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", font="lucida 35 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", font="lucida 35 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()

b = Button(f, text="3", font="lucida 35 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", font="lucida 35 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1", font="lucida 35 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()

b = Button(f, text="0", font="lucida 35 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=27, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", font="lucida 35 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="*", font="lucida 35 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()

b = Button(f, text="/", font="lucida 35 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=16, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="%", font="lucida 35 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=", font="lucida 35 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f = Frame(root, bg="grey")
f.pack()

b = Button(f, text="C", font="lucida 35 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="+", font="lucida 35 bold", padx=28, pady=15)
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)




root.mainloop()