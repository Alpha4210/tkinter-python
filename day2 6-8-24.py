#NOTES ->

#Widgets are the basic building blocks for graphical user interface (GUI) applications. Each GUI component (e.g., buttons, labels) is a widget that is placed somewhere within a user interface window or is displayed as an independent window. 

#Tkinter also offers access to the widgets' geometric configuration, which can organize the widgets in the parent windows. There are mainly three geometry manager classes.
# pack() method: It organizes the widgets in blocks before placing them in the parent widget.
# grid() method: Before placing them in the parent widget, it organizes the widgets in the grid (table-like structure).
# place() method: It organizes the widgets by placing them on specific positions directed by the programmer.

# In Python, almost every widget object has several attributes. Here, we’ll talk about standard widget attributes, including cursors, reliefs, colors, and fonts :-
# Tkinter Widget state: The state of the widget is defined by state attributes. NORMAL, ACTIVE, and DISABLED are the values of the attributes.
# Tkinter Widget padding: padx and pady –these two attributes come under the category of widget padding, and they are responsible for adding extra horizontal and vertical space to the widget. The padx and pady attributes add space between the buttons.
# Tkinter Background colors: The background colors of widgets can be set with the background attributes. It can be abbreviated to bg.
# Width &Height: The width and height attributes set the width and height of the widget.
# Tkinter Fonts: For working with fonts, it has a font module. It has some built-in fonts such as TkTooltipFont, TkDefaultFont.
# Tkinter Cursors: The cursor in Tkinter is set with the cursor
# Tkinter Reliefs: A relief is a border decoration. The possible values are SUNKEN, RAISED, GROOVE, RIDGE, and FLAT.

#CODE ->

from tkinter import *
from PIL import Image, ImageTk #Used to take jpg files in tkinter

root = Tk()

root.geometry("1920x1080") #used to give default dimensions to the application given in widthxheight.

# root.minsize(200,100) #Used to give minimum size to the application window, given in width, height

# root.maxsize(800,900) #Used to give minimum size to the application window, given in width, height

# a = Label(text="YOOO this is just a label") #display text or image on the gui window
# a.pack() #this is to be done, just a rule

# photo = PhotoImage(file="download.jpeg") #Used to give path of image to use

# for jpg images
image = Image.open("download.jpeg")
photo = ImageTk.PhotoImage(image)
    
a = Label(image=photo) #Used to put image on gui window
a.pack()

root.mainloop()




#Videos - 4, 5, 6.