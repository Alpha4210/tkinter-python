# # # from tkinter import *

# # # root = Tk()
# # # root.geometry("655x333")

# # # def hello():
# # #     print("Hello World")

# # # frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
# # # frame.pack(side=LEFT, anchor=NW)

# # # b1 = Button(frame,  fg="red", text="print now", command=hello) #We can create a button using Button(). In command we give a function name which is performed once the button is pressed.

# # # b1.pack(side=LEFT, anchor=NW, padx="20")

# # # b2 = Button(frame,  fg="red", text="print now")
# # # b2.pack(side=LEFT, anchor=NW, padx="20")

# # # b3 = Button(frame,  fg="red", text="print now")
# # # b3.pack(side=LEFT, anchor=NW, padx="20")

# # # b4 = Button(frame,  fg="red", text="print now")
# # # b4.pack(side=LEFT, anchor=NW, padx="20")

# # # root.mainloop()

# # from tkinter import *

# # root = Tk()
# # root.geometry("655x333")

# # def getvals():
# #     print(f"The username is {uservalue.get()}")
# #     print(f"The password is {passvalue.get()}")

# # user = Label(root, text="Username")
# # password = Label(root,  text="Password")
# # user.grid() # Display the element inf orm a grid.
# # password.grid(row=1) #The attributes given in grid are row and column.

# # # Variable classes in tkinter - BooleanVar, DoublVar, IntVar, StringVar.

# # uservalue = StringVar() #Forms a string var variable class
# # passvalue = StringVar()

# # userentry = Entry(root, textvariable= uservalue) # Makes a input like element where we can enter our data.
# # passentry = Entry(root, textvariable= passvalue)
# # userentry.grid(row=0, column=1)
# # passentry.grid(row=1, column=1)

# # Button(text="Submit", command=getvals).grid() #A one liner button.

# # root.mainloop()

# # #Quick quiz - A form for a dance class and write the data in a file.

# from tkinter import *
# root = Tk()
# root.geometry("644x344")

# def getvals():
#     print("Submitted sucessfully")


# #heading
# Label(root, text="Welcome to Parth travels", font="comicsans 13 bold", pady=15).grid(row=0, column=3)

# #Text for our form
# name = Label(root, text="Name")
# phone = Label(root, text="phone")
# gender = Label(root, text="gender")
# emergency = Label(root, text="Emergency Contact")
# payment = Label(root, text="Payment mode")
# #Packing of text values
# name.grid(row=1, column=2)
# phone.grid(row=2, column=2)
# gender.grid(row=3, column=2)
# emergency.grid(row=4, column=2)
# payment.grid(row=5, column=2)

# #Tkinter variables for storing entries
# namevalue = StringVar()
# phonevalue = StringVar()
# gendervalue = StringVar()
# emergencyvalue = StringVar()
# paymentvalue = StringVar()
# foodservicevalue = IntVar()

# #Entries for our form
# nameentry = Entry(root, textvariable=namevalue)
# phoneentry = Entry(root, textvariable=phonevalue)
# genderentry = Entry(root, textvariable=gendervalue)
# emergencyentry = Entry(root, textvariable=emergencyvalue)
# paymententry = Entry(root, textvariable=paymentvalue)

# #Packing the entries for our form
# nameentry.grid(row=1, column=3)
# phoneentry.grid(row=2, column=3)
# genderentry.grid(row=3, column=3)
# emergencyentry.grid(row=4, column=3)
# paymententry.grid(row=5, column=3)

# #checkbox and packing it
# foodservice = Checkbutton(text="Want to prebook your meals?", variable=foodservicevalue)
# foodservice.grid(row=6, column=3)

# #Button, packing it and assigning it a command
# Button(text="Submit it to Parth Travels", command=getvals).grid(row=7, column=3)


# root.mainloop()

# # # # Videos - 10, 11, 12.