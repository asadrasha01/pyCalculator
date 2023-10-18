from tkinter import *

window = Tk()
window.title("Calculator")
#Buttons
clear_btn = Button(window, text="Clear")
clear_btn.pack()

exponentiation_btn = Button(window, text="E^x")
exponentiation_btn()

add_btn = Button(window, text="+")
add_btn()

subtract_btn = Button(window, text="-")
subtract_btn()

multiply_btn = Button(window, text="*")
multiply_btn()

divide_btn = Button(window, text="/")
divide_btn()

display = Entry(window,justify=RIGHT)

display.pack(side=TOP, expand=YES, fill=BOTH)

window.mainloop