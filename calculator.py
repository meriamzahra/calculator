# import module
import tkinter as tk
from widgets import ReadOnlyText

# create object
root = tk.Tk()

# setting the minimum size of the root window
root.minsize(300, 300)


# specify text field
text_result = ReadOnlyText(root, height=2, width=16, font=["Arial", 24])
text_result.grid(column=0, columnspan=4, sticky="NSEW")


# specify grid
tk.Widget.rowconfigure(root, 0, weight=1)
tk.Widget.rowconfigure(root, 1, weight=1)
tk.Widget.rowconfigure(root, 2, weight=1)
tk.Widget.rowconfigure(root, 3, weight=1)
tk.Widget.rowconfigure(root, 4, weight=1)
tk.Widget.rowconfigure(root, 5, weight=1)
tk.Widget.columnconfigure(root, "all", weight=1)


# initialise variables
calculation = ""


# define functions
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation

    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "ERROR")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


# create buttons and set grid
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), font=["Arial", 14], width=5)
btn_1.grid(row=1, column=0, sticky="NSEW")
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), font=["Arial", 14], width=5)
btn_2.grid(row=1, column=1, sticky="NSEW")
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), font=["Arial", 14], width=5)
btn_3.grid(row=1, column=2, sticky="NSEW")
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), font=["Arial", 14], width=5)
btn_4.grid(row=2, column=0, sticky="NSEW")
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), font=["Arial", 14], width=5)
btn_5.grid(row=2, column=1, sticky="NSEW")
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), font=["Arial", 14], width=5)
btn_6.grid(row=2, column=2, sticky="NSEW")
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), font=["Arial", 14], width=5)
btn_7.grid(row=3, column=0, sticky="NSEW")
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), font=["Arial", 14], width=5)
btn_8.grid(row=3, column=1, sticky="NSEW")
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), font=["Arial", 14], width=5)
btn_9.grid(row=3, column=2, sticky="NSEW")
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), font=["Arial", 14], width=5)
btn_0.grid(row=4, column=1, sticky="NSEW")
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), font=["Arial", 14], width=5)
btn_plus.grid(row=1, column=3, sticky="NSEW")
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), font=["Arial", 14], width=5)
btn_minus.grid(row=2, column=3, sticky="NSEW")
btn_multiply = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), font=["Arial", 14], width=5)
btn_multiply.grid(row=3, column=3, sticky="NSEW")
btn_divide = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), font=["Arial", 14], width=5)
btn_divide.grid(row=4, column=3, sticky="NSEW")
btn_left_parentheses = tk.Button(root, text="(", command=lambda: add_to_calculation("("), font=["Arial", 14], width=5)
btn_left_parentheses.grid(row=4, column=0, sticky="NSEW")
btn_right_parentheses = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), font=["Arial", 14], width=5)
btn_right_parentheses.grid(row=4, column=2, sticky="NSEW")
btn_equals = tk.Button(root, text="=", command=lambda: evaluate_calculation(), font=[14], width=12)
btn_equals.grid(row=5, column=2, columnspan=2, sticky="NSEW")
btn_clear = tk.Button(root, text="C", command=lambda: clear_field(), font=[14], width=12)
btn_clear.grid(row=5, column=0, columnspan=2, sticky="NSEW")


# execute tkinter
root.mainloop()
