import tkinter as tk

calculation = ""

def calculation_elements(symbol):
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
        clear_input()
        text_result.insert(1.0, "Error")

def delete_last_character():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def clear_input():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

m = tk.Tk()
m.geometry("330x280")
m.title ("Calculator")

text_result = tk.Text(m, height=1, width=15, font=('Poppins', 24), borderwidth=3, relief="sunken")
text_result.grid(pady=10, columnspan=5, padx=20)

btn_7 = tk.Button(m, text="7", command=lambda:calculation_elements(7), width=5, font=('Poppins', 14))
btn_7.grid(row=2, column=1)
btn_8 = tk.Button(m, text="8", command=lambda:calculation_elements(8), width=5, font=('Poppins', 14))
btn_8.grid(row=2, column=2)
btn_9 = tk.Button(m, text="9", command=lambda:calculation_elements(9), width=5, font=('Poppins', 14))
btn_9.grid(row=2, column=3)
btn_4 = tk.Button(m, text="4", command=lambda:calculation_elements(4), width=5, font=('Poppins', 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(m, text="5", command=lambda:calculation_elements(5), width=5, font=('Poppins', 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(m, text="6", command=lambda:calculation_elements(6), width=5, font=('Poppins', 14))
btn_6.grid(row=3, column=3)
btn_1 = tk.Button(m, text="1", command=lambda:calculation_elements(1), width=5, font=('Poppins', 14))
btn_1.grid(row=4, column=1)
btn_2 = tk.Button(m, text="2", command=lambda:calculation_elements(2), width=5, font=('Poppins', 14))
btn_2.grid(row=4, column=2)
btn_3 = tk.Button(m, text="3", command=lambda:calculation_elements(3), width=5, font=('Poppins', 14))
btn_3.grid(row=4, column=3)
btn_0 = tk.Button(m, text="0", command=lambda:calculation_elements(0), width=5, font=('Poppins', 14))
btn_0.grid(row=5, column=2)
btn_mul = tk.Button(m, text="*", command=lambda:calculation_elements("*"), width=5, font=('Poppins', 14))
btn_mul.grid(row=2, column=4)
btn_div = tk.Button(m, text="/", command=lambda:calculation_elements("/"), width=5, font=('Poppins', 14))
btn_div.grid(row=3, column=4)
btn_minus = tk.Button(m, text="-", command=lambda:calculation_elements("-"), width=5, font=('Poppins', 14))
btn_minus.grid(row=4, column=4)
btn_plus = tk.Button(m, text="+", command=lambda:calculation_elements("+"), width=5, font=('Poppins', 14))
btn_plus.grid(row=5, column=4)
btn_dot = tk.Button(m, text=".", command=lambda:calculation_elements("."), width=5, font=('Poppins', 14))
btn_dot.grid(row=6, column=1)
btn_open = tk.Button(m, text="(", command=lambda:calculation_elements("("), width=5, font=('Poppins', 14))
btn_open.grid(row=5, column=1)
btn_close = tk.Button(m, text=")", command=lambda:calculation_elements(")"), width=5, font=('Poppins', 14))
btn_close.grid(row=5, column=3)
btn_clear = tk.Button(m, text="C", command=clear_input, width=5, font=('Poppins', 14), bg="red",fg="white")
btn_clear.grid(row=6, column=2)
btn_del = tk.Button(m, text="DEL", command=delete_last_character, width=5, font=('Poppins', 14), bg="red",fg="white")
btn_del.grid(row=6, column=3)
btn_equals = tk.Button(m, text="=", command=evaluate_calculation, width=5, font=('Poppins', 14), bg="green",fg="white")
btn_equals.grid(row=6, column=4, columnspan=1)

m.mainloop()

