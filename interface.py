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

zero_btn = Button(window, text="0")
zero_btn()

one_btn = Button(window, text="1")
one_btn()

two_btn = Button(window, text="2")
two_btn()

three_btn = Button(window, text="3")
three_btn()

four_btn = Button(window, text="4")
four_btn()

five_btn = Button(window, text="5")
five_btn()

six_btn = Button(window, text="6")
six_btn()

seven_btn = Button(window, text="7")
seven_btn()

eight_btn = Button(window, text="8")
eight_btn()

nine_btn = Button(window, text="9")
nine_btn()

equal_btn = Button(window, text="=")
equal_btn()

display = Entry(window,justify=RIGHT)

display.pack(side=TOP, expand=YES, fill=BOTH)

window.mainloop