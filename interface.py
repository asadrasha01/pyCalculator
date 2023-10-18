from tkinter import *

window = Tk()
window.title("Calculator")
#Buttons
clear_btn = Button(window, text="Clear")
clear_btn.pack()

exponentiation_btn = Button(window, text="E^x")
exponentiation_btn()


display = Entry(window,justify=RIGHT)

display.pack(side=TOP, expand=YES, fill=BOTH)

window.mainloop