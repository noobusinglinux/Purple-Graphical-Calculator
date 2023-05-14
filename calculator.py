import tkinter as tk

# Create the tkinter window
window = tk.Tk()
window.title("Graphical Calculator")

# Change the background color of the window
window.configure(bg='purple')

# Set the golden yellow color in hexadecimal format
golden_yellow = '#FFD700'

# Create the input field
input_field = tk.Entry(window, width=50, borderwidth=5)
input_field.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Define button click and clear functions
def button_click(number):
    current = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(0, str(current) + str(number))

def button_clear():
    input_field.delete(0, tk.END)

def button_add():
    first_number = input_field.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = float(first_number)
    input_field.delete(0, tk.END)

def button_subtract():
    first_number = input_field.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = float(first_number)
    input_field.delete(0, tk.END)

def button_multiply():
    first_number = input_field.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = float(first_number)
    input_field.delete(0, tk.END)

def button_divide():
    first_number = input_field.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = float(first_number)
    input_field.delete(0, tk.END)

def button_equal():
    second_number = input_field.get()
    input_field.delete(0, tk.END)

    if math_operation == "addition":
        input_field.insert(0, f_num + float(second_number))
    elif math_operation == "subtraction":
        input_field.insert(0, f_num - float(second_number))
    elif math_operation == "multiplication":
        input_field.insert(0, f_num * float(second_number))
    elif math_operation == "division":
        input_field.insert(0, f_num / float(second_number))

# Create the number buttons
button_1 = tk.Button(window, text="1", padx=40, pady=20, bg=golden_yellow, fg='black', command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=40, pady=20, bg=golden_yellow, fg='black', command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=40, pady=20, bg=golden_yellow, fg='black', command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=40, pady=20, bg=golden_yellow, fg='black', command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=40, pady=20, bg=golden_yellow, fg='black', command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=40, pady=20, bg=golden_yellow, fg='black', command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=40, pady=20, bg=golden_yellow, fg='black', command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=40, pady=20, bg=golden_yellow, fg='black', command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=40, pady=20, bg=golden_yellow, fg='black', command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=40, pady=20, bg=golden_yellow, fg='black', command=lambda: button_click(0))

# Create the operation buttons
button_add = tk.Button(window, text="+", padx=39, pady=20, bg=golden_yellow, fg='black', command=button_add)
button_subtract = tk.Button(window, text="-", padx=41, pady=20, bg=golden_yellow, fg='black', command=button_subtract)
button_multiply = tk.Button(window, text="*", padx=40, pady=20, bg=golden_yellow, fg='black', command=button_multiply)
button_divide = tk.Button(window, text="/", padx=41, pady=20, bg=golden_yellow, fg='black', command=button_divide)
button_equal = tk.Button(window, text="=", padx=91, pady=20, bg=golden_yellow, fg='black', command=button_equal)
button_clear = tk.Button(window, text="Clear", padx=79, pady=30, bg=golden_yellow, fg='black', command=button_clear)

# Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_equal.grid(row=5, column=1, columnspan=2)

# Run the window
window.mainloop()
