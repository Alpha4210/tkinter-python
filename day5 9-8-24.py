# # from tkinter import *
# # root = Tk()
# # root.geometry("644x344")

# # def getvals():
# #     print("Submitting form")
# #     print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get(),foodservicevalue.get()}")
# #     with open("records.txt","w") as f: #Used to make a file to store our data.
# #         f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get(),foodservicevalue.get()}\n")


# # #heading
# # Label(root, text="Welcome to Parth travels", font="comicsans 13 bold", pady=15).grid(row=0, column=3)

# # #Text for our form
# # name = Label(root, text="Name")
# # phone = Label(root, text="phone")
# # gender = Label(root, text="gender")
# # emergency = Label(root, text="Emergency Contact")
# # payment = Label(root, text="Payment mode")
# # #Packing of text values
# # name.grid(row=1, column=2)
# # phone.grid(row=2, column=2)
# # gender.grid(row=3, column=2)
# # emergency.grid(row=4, column=2)
# # payment.grid(row=5, column=2)

# # #Tkinter variables for storing entries
# # namevalue = StringVar()
# # phonevalue = StringVar()
# # gendervalue = StringVar()
# # emergencyvalue = StringVar()
# # paymentvalue = StringVar()
# # foodservicevalue = IntVar()

# # #Entries for our form
# # nameentry = Entry(root, textvariable=namevalue)
# # phoneentry = Entry(root, textvariable=phonevalue)
# # genderentry = Entry(root, textvariable=gendervalue)
# # emergencyentry = Entry(root, textvariable=emergencyvalue)
# # paymententry = Entry(root, textvariable=paymentvalue)

# # #Packing the entries for our form
# # nameentry.grid(row=1, column=3)
# # phoneentry.grid(row=2, column=3)
# # genderentry.grid(row=3, column=3)
# # emergencyentry.grid(row=4, column=3)
# # paymententry.grid(row=5, column=3)

# # #checkbox and packing it
# # foodservice = Checkbutton(text="Want to prebook your meals?", variable=foodservicevalue)
# # foodservice.grid(row=6, column=3)

# # #Button, packing it and assigning it a command
# # Button(text="Submit it to Parth Travels", command=getvals).grid(row=7, column=3)


# # root.mainloop()

# from tkinter import *
# root =  Tk()

# canvas_width = 800
# canvas_height = 400

# root.geometry(f"{canvas_width}x{canvas_height}")
# can_widget = Canvas(root, width=canvas_width, height=canvas_height) # Canvas is used to create figures.
# can_widget.pack()

# # The line goes from point x1, y1 to x2, y2.
# can_widget.create_line(0,0,800,400, fill="red") #(x1, y1, x2, y2) #Used to create a line.
# #fill is used to color the shape
# can_widget.create_rectangle(300,200,100,300) #Top-left cords, Bottom-right cords #Used to create a rectangle.

# can_widget.create_text(200, 200, text="Hello world") #center coordinates of the text #Used to write text at certain position.

# can_widget.create_oval(344, 133, 244, 350) #for coordinates png file. #Used to create oval.


# root.mainloop()

from tkinter import *

def parth(event):
    print(f"You clicked on the button at {event.x}, {event.y}.") #tells the coordinate where the button was pressed.

root = Tk()
root.title("Events")
root.geometry("644x334")

widget = Button(root, text="Click me")
widget.pack()
#Event - anything you do on a computer is basically an event.

widget.bind('<Button-1>', parth) #used to bind an event to the button
widget.bind('<Double-1>', quit) #when the left event occurs then the right function is executed.
root.mainloop()

#Mini project 1 - Using news API create a gui to read news.


# # # Videos - 13, 14, 15, 16, 17