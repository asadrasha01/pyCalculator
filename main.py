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
    btn.grid(row=(i // 3 + 1)+1, column=i % 3)

btn_plus = tk.Button(root, text='+', command=lambda: add_to_calculation('+'), width=5, font=('Arial', 14))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text='-', command=lambda: add_to_calculation('-'), width=5, font=('Arial', 14))
btn_minus.grid(row=3, column=4)
btn_mul = tk.Button(root, text='*', command=lambda: add_to_calculation('*'), width=5, font=('Arial', 14))
btn_mul.grid(row=4, column=4)
btn_div = tk.Button(root, text='/', command=lambda: add_to_calculation('/'), width=5, font=('Arial', 14))
btn_div.grid(row=5, column=4)
btn_open_p = tk.Button(root, text='(', command=lambda: add_to_calculation('('), width=5, font=('Arial', 14))
btn_open_p.grid(row=5, column=0)
btn_close_p = tk.Button(root, text=')', command=lambda: add_to_calculation(')'), width=5, font=('Arial', 14))
btn_close_p.grid(row=5, column=2)
btn_clear = tk.Button(root, text='C', command=clear_field, width=10, font=('Arial', 14))
btn_clear.grid(row=6, column=0, columnspan=2)
btn_equal = tk.Button(root, text='=', command=evaluate_calculation, width=10, font=('Arial', 14))
btn_equal.grid(row=6, column=2, columnspan=2)

btn0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=('Arial', 14))
btn0.grid(row=5, column=1)


root.mainloop()
