from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("stoplight window")

#Set size of window
root.geometry("500x500")

# Create buttons
red_button = Button(root, text="Red", background='red')
yellow_button = Button(root, text="Yellow", background='yellow')
green_button = Button(root, text="Green", background='green')

#textbox
l = Label(text = "What color is the light? ")
inputtxt = Text(root, height = 10,
                width = 25)



#Add a label
label = Label(root, text="CHANGE ME!")


# Place widgets in window (with pack function!)
red_button.grid(row = 0, column =0)
yellow_button.grid(row =0, column =3)
green_button.grid(row =0, column =6)
l.grid(row = 2,column =3)
inputtxt.grid(row = 4, column =3)



# Start the GUI event loop
root.mainloop()