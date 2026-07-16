import tkinter as tk 

root= tk.Tk()
root.title("Calculator")
root.geometry("400x550")

for i in range(5):
    root.grid_rowconfigure(i, weight=1)

for j in range(4):
    root.grid_columnconfigure(j, weight=1)

entry = tk.Entry(root, font=("Arial", 20, "bold"), justify="right", bd=10, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=12, sticky="ew")

def press(value):
    entry.insert(tk.END, value)

button1 = tk.Button(
    root, text="1",
    font=("Arial", 18, "bold"), 
    command=lambda: press("1"),
    bd=2,
    relief="solid",
    borderwidth=2
)

button1.grid(row=1, column=0, padx=2, pady=5, sticky="nsew")

button2 = tk.Button(
    root, text="2",
    font=("Arial", 18, "bold"),
    command=lambda: press("2"),
    bd=2,
    relief="solid",
    borderwidth=2
)

button2.grid(row=1, column=1, padx=2, pady=5, sticky="nsew")

button3 = tk.Button(
     root, text="3",
     font=("Arial",18, "bold"),
     command=lambda: press("3"),
     bd=2,
    relief="solid",
    borderwidth=2
)

button3.grid(row=1, column=2, padx=2, pady=5, sticky="nsew")

button4 = tk.Button(
    root, text="4",
    font=("Arial", 18, "bold"),
    command=lambda: press("4"),
    bd=2,
    relief="solid",
    borderwidth=2
)

button4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

button5 = tk.Button(
    root, text="5",
    font=("Arial", 18, "bold"),
    command=lambda: press("5"),
    bd=2,
    relief="solid",
    borderwidth=2
)

button5.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

button6 = tk.Button(
    root, text="6",
    font=("Arial", 18, "bold"),
    command=lambda: press("6"),
    bd=2,
    relief="solid",
    borderwidth=2
)

button6.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

button7 = tk.Button(
    root, text="7",
    font=("Arial", 18, "bold"),
    command=lambda: press("7"),
    bd=2,
    relief="solid",
    borderwidth=2
)

button7.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

button8 = tk.Button(
    root, text="8",
    font=("Arial", 18, "bold"),
    command=lambda: press("8"),
    bd=2,
    relief="solid",
    borderwidth=2
)

button8.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

button9 = tk.Button(
    root,text="9",
    font=("Arial", 18, "bold"),
    command=lambda: press("9"),
    bd=2,
    relief="solid",
    borderwidth=2
)

button9.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

button0 = tk.Button(
    root,text="0",
    font=("Arial", 18, "bold"),
    command=lambda: press("0"),
    bd=2,
    relief="solid",
    borderwidth=2
)

button0.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

multiply = tk.Button(
    root,text="*",
    font=("Arial", 18, "bold"),
    command=lambda: press("*"),
    bd=2,
    relief="solid",
    borderwidth=2
)

multiply.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

plus = tk.Button(
    root,text="+",
    font=("Arial", 18, "bold"),
    command=lambda: press("+"),
    bd=2,
    relief="solid",
    borderwidth=2
)

plus.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

minus = tk.Button(
    root,text="-",
    font=("Arial", 18, "bold"),
    command=lambda: press("-"),
    bd=2,
    relief="solid",
    borderwidth=2
)

minus.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

divide = tk.Button(
    root,text="/",
    font=("Arial", 18, "bold"),
    command=lambda: press("/"),
    bd=2,
    relief="solid",
    borderwidth=2
)

divide.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

def clear():
    entry.delete(0, tk.END)

clear = tk.Button(
   root,text="C",
   font=("Arial", 18, "bold"),
   command=clear,
   bd=2,
    relief="solid",
    borderwidth=2
)

clear.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

equal = tk.Button(
    root,text="=",
    font=("Arial", 18, "bold"),
    command=equal,
    bd=2,
    relief="solid",
    borderwidth=2
)

equal.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

root.mainloop()



