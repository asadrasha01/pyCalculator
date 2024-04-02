import ast
import tkinter as tk

calculation = ''


# Functions
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    calculator_result.delete(1.0, 'end')
    calculator_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(ast.literal_eval()(calculation))
        calculator_result.delete(1.0, 'end')
        calculator_result.insert(1.0, calculation)
    except:
        clear_field()
        calculator_result.insert(1.0, 'Error')


def clear_field():
    global calculation
    calculation = ''
    calculator_result.delete(1.0, 'end')


# Interface
# The applications
root = tk.Tk()
root.geometry('300x275')

# Text display
calculator_result = tk.Text(root, height=2, width=16, font=('Arial', 24))
calculator_result.grid(columnspan=5)

# Buttons
for i in range(9):
    btn = tk.Button(root, text=str(i + 1), command=lambda x=i + 1: add_to_calculation(x), width=5, font=('Arial', 14))
    btn.grid(row=i // 3 + 1, column=i % 3)

btn0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=('Arial', 14))
btn0.grid(row=4, column=0, columnspan=2)

root.mainloop()
