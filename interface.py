from tkinter import *
from tkinter import PhotoImage
import subprocess

applescript = """
tell application "Finder"
    set myApp to POSIX file "<full_path_to_your_script>"
    set myIcon to POSIX file "<full_path_to_your_icns_icon>"

    set myAlias to myApp as alias
    set myIconAlias to myIcon as alias

    set icon of myAlias to myIconAlias
end tell
"""

subprocess.run(['osascript', '-e', applescript])
window = Tk()
window.title("Calculator")

def btn_click(number):
    current = str(display.get())
    display.delete(0, END)
    display.insert(0, current + str(number))

def btn_clear():
    display.delete(0, END)

def btn_equal():
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, END)
        display.insert(0, result)
    except Exception as e:
        display.delete(0, END)
        display.insert(0, "Error")

for i in range(10):
    btn = Button(window, text=str(i), command=lambda i=i: btn_click(i))
    btn.grid(row=i//3+1, column=i%3)

add_btn = Button(window, text="+", command=lambda: btn_click('+'))
add_btn.grid(row=1, column=3)

subtract_btn = Button(window, text="-", command=lambda: btn_click('-'))
subtract_btn.grid(row=2, column=3)

multiply_btn = Button(window, text="*", command=lambda: btn_click('*'))
multiply_btn.grid(row=3, column=3)

divide_btn = Button(window, text="/", command=lambda: btn_click('/'))
divide_btn.grid(row=4, column=3)

equal_btn = Button(window, text="=", command=btn_equal)
equal_btn.grid(row=4, column=2)

exponentiation_btn = Button(window, text="E^x", command=lambda: btn_click('**'))
exponentiation_btn.grid(row=4, column=1)

modulus_btn = Button(window, text="%", command=lambda: btn_click('%'))
modulus_btn.grid(row=5, column=1)

clear_btn = Button(window, text="C", command=btn_clear)
clear_btn.grid(row=5, column=2)

display = Entry(window, justify=RIGHT)
display.grid(row=0, column=0, columnspan=4)

window.iconbitmap(default='image.icns')

window.mainloop()

