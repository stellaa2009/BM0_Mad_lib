from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()

#Set size of window
root.geometry("300x150")

# Create buttons
red_button = Button(root, text="Red", background='red')
yellow_button = Button(root, text="Yellow", background='yellow')
green_button = Button(root, text="Green", background='green')



#Add a label
label = Label(root, text="CHANGE ME!")

# Place widgets in window (with pack function!)
label.pack()
red_button.pack(side = TOP)
yellow_button.pack( side = TOP)
green_button.pack( side = TOP)



# Start the GUI event loop
root.mainloop()