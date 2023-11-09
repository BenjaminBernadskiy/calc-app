import tkinter as tk

root = tk.Tk()
root.title("Simple Calculater")
root.geometry("300x400")

display_frame = tk.Frame(root, width=300, height=50, bg="gray")
display_frame.pack()

display = tk.Entry(display_frame,font=("Ariel", 20) ,insertwidth=4, width=14, justify="center")
display.pack(padx=10, pady=30)

def update_display(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current+value)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

for i in range(1, 10):
    btn = tk.Button(buttons_frame, text=str(i), padx=20, pady=10, command=lambda i=i: update_display(str(i)))
    btn.grid(row=2 + (i-1) // 3, column=(i-1) % 3)

btnzero = tk.Button(buttons_frame, text="0", padx=20, pady=10, command=lambda i=i: update_display("0"))
btnzero.grid(row=5, column=0)

btndot = tk.Button(buttons_frame, text=".", padx=20, pady=10, command=lambda i=i: update_display("."))
btndot.grid(row=5, column=1)


def add():
    pass

def subtract():
    pass

def multiply():
    pass

def divide():
    pass

btn_add = tk.Button(buttons_frame, text="+", padx=20, pady=10, command=add)
btn_add.grid(row=2, column=3)

btn_add = tk.Button(buttons_frame, text="-", padx=20, pady=10, command=subtract)
btn_add.grid(row=3, column=3)

btn_add = tk.Button(buttons_frame, text="*", padx=20, pady=10, command=multiply)
btn_add.grid(row=4, column=3)

btn_add = tk.Button(buttons_frame, text="/", padx=20, pady=10, command=divide)
btn_add.grid(row=5, column=3)

def square():
    pass

def inverse():
    pass

def negate():
    pass

btn_square = tk.Button(buttons_frame, text="x^2", padx=20, pady=10, command=square)
btn_square.grid(row=1, column=1)

btn_inverse = tk.Button(buttons_frame, text="1/x", padx=20, pady=10, command=inverse)
btn_inverse.grid(row=1, column=2)

btn_negate = tk.Button(buttons_frame, text="+/-", padx=20, pady=10, command=negate)
btn_negate.grid(row=1, column=3)

def clear():
    pass

def equal():
    pass

btn_clear = tk.Button(buttons_frame, text="C", padx=20, pady=10, command=clear)
btn_clear.grid(row=1, column=0)

btn_equal = tk.Button(buttons_frame, text="=", padx=20, pady=10, command=equal)
btn_equal.grid(row=5, column=2)

root.mainloop()