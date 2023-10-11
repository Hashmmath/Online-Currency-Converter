# AP20110010809
# Hashmmath Shaik
# CSE-L

from tkinter import *  # Using tkinter library to generate a GUI application

from tkinter.ttk import Combobox  # A combobox allows you to select one value in a list of values
# The basic functionality of tkinter.ttk is to separate the Data, to the extent possible

from google_currency import convert
# A simple library to convert the currency of one country to other, it supports 153 countries' currency

import json  # JSON (JavaScript Object Notation) is commonly used for transmitting data in web applications

from tkinter import messagebox

# There is a option of messagebox in TKINTER to display a dialogue box in case of error or Warning

root = Tk()  # Tk root widget, which is a window with a title bar and other decoration provided by the window manager.
# The root widget has to be created before any other widgets and there can only be one root widget.

root.geometry("700x425")  # For setting the size of the Application
root.title("CURRENCY CONVERTER")  # The Name of the Application
root.config(bg="black")  # Selecting the Background of the Application

with open("Currency.txt") as f:  # using file handling to take the currencies that are in the form of text
    lines = f.readlines()  # readlines() function uses to read each and every line of the text file

dicttop = {}  # declaring a dicttop variable for creating a dictionary

for line in lines:  # for specifically taking the required point from the file in this case it is the LINES.
    opaque = line.split("\t")
    # Split() function is used to split the lines that are given in the txt file with countries’ currencies
    dicttop[opaque[1]] = opaque[2]  # in this declaration we are declaring two list having same DATA
    # with the column numbers(1&2) in the file ind.txt


def functionbutton():  # defining a function functionbutton() for the convert button to convert the currency
    try:  # The try block is used to check some code for errors
        # the code inside the try block will execute when there is no error in the program

        Box1 = Combobox1.get()  # The Box1 is declared as combobox as it contains one set of the currencies
        # but has a selecting option for the user like the main functionality of combobox
        # the get() function takes the Input or the selected currency given by the user

        Box2 = Combobox2.get()  # The Box2 is declared as combobox as it contains same set of currencies
        # but has a selecting option for the user like the main functionality of combobox
        # the get() function takes the Input or the selected currency given by the user

        laptop = dicttop[Box1]  # declaring any variable to take the respected value from the list
        laptip = dicttop[Box2]  # declaring any variable to take the respected value from the list
        serial = var1.get()  # get() function takes the amount value given by the user where var1 is declared
        opol = convert(laptop, laptip, serial)  # convert() is used to convert specific set of inputs
        # like the from and to currencies and also the amount inputs given by the user
        load = json.loads(opol)  # json is a subset of JavaScript syntax used as a lightweight interchange format
        amount = load["amount"]  # "amount" is used to only print the amount rather than anyother data
        var2.set(amount)  # set() function assigns the answer that is the converted value to the respective box in
        # which the output will be printed or displayed

    except:  # if the try block catches error it gets directed into except block and displays the error if any given
        rr = messagebox.askretrycancel("A Problem Has Been Occurred",
                                       "Please Check your Internet Connection or Check the Amount You Have Entered.")
        # message box in the sense dialogue box for any error or loss of internet


Title = Label(root, text="MODERN CURRENCY CONVERTER", fg="RED", bg="BLACK", font=("Arial Black", 19, "italic"))
# For giving Title Inside the Application.

Title.place(x=110, y=10)  # Position of the Title in the Applicaion

Lable1 = Label(root, text="Enter the Amount to Convert :-", bg="Black", fg="Green",
               font=("Arial Black", 17, "italic", "bold"))
# Text for intimating the user to give the Input Amount

Lable1.place(x=10, y=60)  # Position of the Message for the User Intimation

var1 = IntVar()  # Declaring the Input Variable As String the Int represents to give as Integer form only
feeder = Entry(root, width=26, text=var1, bg="white", fg="maroon", font=("cambaria math", 15, "bold"))
# Generating a BOX or Section for giving Input Amount. Here,FEEDER is used for Taking Input from User like "scanf" in C.

feeder.place(x=405, y=67)  # Position of the BOX or Sector for Giving Input Money

Label2 = Label(root, text="Select the Currency to Convert Your Amount From :- ", bg="black", fg="orange",
               font=("calibri", 15, "bold", "italic"))
# Gives the User a chance to select the Currency to convert the amount

Label2.place(x=15, y=120)  # Position of the Message for the user Intimation.

slider = StringVar()  # This is declared as the way of giving the input as a option
Combobox1 = Combobox(root, width=23, textvariable=slider, state="readonly", font=("calibri", 13, "bold"))
# readonly function is used to take the values or information only for the purpose of using them not to edit them
Combobox1['values'] = [item for item in dicttop.keys()]
# The combobox 1 contains the name and information related to the currencies

Combobox1.current(4)  # the 4 is the indexing value taken by the python from the txt file for default currency
Combobox1.place(x=463, y=125)  # position of the box for selecting currency

Lable3 = Label(root, text="Select the Currency to Convert Your Amount To     :-  ", bg="black", fg="light blue",
               font=("calibri", 15, "bold", "italic"))
# Gives the User a chance to select the Currency to convert the amount

Lable3.place(x=15, y=180)  # Position of the Message for the user Intimation in the application

foreground = StringVar()  # declaring a variable as string
Combobox2 = Combobox(root, width=23, textvariable=foreground, state="readonly", font=("calibri", 13, "bold"))
# readonly function is used to take the values or information only for the purpose of using them not to edit them
Combobox2['values'] = [item for item in dicttop.keys()]
# The combobox 2 contains the name and information related to the currencies

Combobox2.current(0)  # the 4 is the indexing value taken by the python from the txt file for default currency
Combobox2.place(x=463, y=185)  # Position of the slider box in the application for selecting currency

Button1 = Button(root, bg="white", text="CONVERT", command=functionbutton, fg="red", font=("arial black", 14, "bold",
                                                                                           "italic"), relief=RAISED,
                 cursor="hand2")
# The button is the main part that runs the calculations and generates the output
# The relief style of a widget refers to certain simulated 3-D effects around the outside of the widget
Button1.place(x=280, y=240)  # position of the button in the application

Label4 = Label(root, text="Converted Amount  :- ", bg="black", fg="maroon", font=("Arial Black", 17, "italic",
                                                                                  "bold"))
# gives the message where the output is printed
Label4.place(x=80, y=300)  # position of the output message in the application

var2 = IntVar()  # declaring variable var2 as a string IntVar()
Entry2 = Entry(root, textvariable=var2, fg="blue", state="readonly", width=26, font=("cambaria math", 15, "bold"))
# gives the calculated output in the box in the format of readonly so that the user cannot change or edit it.
Entry2.place(x=360, y=305)  # Position of the output box in the application

footer = Label(root, text="Designed and Developed by Hashmmath Shaik", bg="black", fg="GOLD",
               font=("Arial Black", 19, "italic"))  # Message box for the AUTHOR
footer.place(x=30, y=360)  # Position of the box in the application

root.mainloop()  # Creates the tkinter widget
