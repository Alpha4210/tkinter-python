from tkinter import *
import tkinter.messagebox as tmb
import csv
root = Tk()
root.geometry("330x500")
def saveval():
    tmb.showinfo("Thank You","Thanks for submitting the form,  we will contact you soon!")
    with open("save_dance_record.csv", "a+") as f:
        x = [namevalue.get(), emailvalue.get(), phonevalue.get(), agevalue.get(), dancevalue.get()]
        fwr = csv.writer(f)
        fwr.writerow(x)
Label(root, text="Dance Form", font="verdana 19 bold").grid(row=0, column=1)

#Text for our form
name = Label(root, text="Name")
email = Label(root, text="Email")
phone = Label(root, text="Phone")
age = Label(root, text="Age")
dance = Label(root, text="Type of dance")

#Packing the text
name.grid(row=1, column=0, pady=13, padx=5)
email.grid(row=2, column=0, pady=13, padx=5)
phone.grid(row=3, column=0, pady=13, padx=5)
age.grid(row=4, column=0, pady=13, padx=5)
dance.grid(row=5, column=0, pady=13, padx=5)

#Variables for storing entries
namevalue = StringVar()
emailvalue = StringVar()
phonevalue = StringVar()
agevalue = StringVar()
dancevalue = StringVar()

#Input box for getting values
nameentry = Entry(root, textvariable=namevalue)
emailentry = Entry(root, textvariable=emailvalue)
phoneentry = Entry(root, textvariable=phonevalue)
ageentry = Entry(root, textvariable=agevalue)
danceentry = Entry(root, textvariable=dancevalue)

#Packing the input boxes
nameentry.grid(row=1, column=1, pady=13, padx=5)
emailentry.grid(row=2, column=1, pady=13, padx=5)
phoneentry.grid(row=3, column=1, pady=13, padx=5)
ageentry.grid(row=4, column=1, pady=13, padx=5)
danceentry.grid(row=5, column=1, pady=13, padx=5)
#Creating input boxes

Button(text="Submit", command=saveval, padx=20, pady=12, bg="lightgreen").grid(row=7, column=1)




root.mainloop()