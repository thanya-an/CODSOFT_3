import tkinter as tk
from tkinter import messagebox

# Function to evaluate expression
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)  # Be cautious: eval is powerful!
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        messagebox.showerror("Error", "Invalid Input")

# Function to add text to entry
def add_to_entry(value):
    entry.insert(tk.END, value)

# Function to clear entry
def clear_entry():
    entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x400")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, width=25, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=8, height=2, bg="green", fg="white", command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=8, height=2, command=lambda t=text: add_to_entry(t)).grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(root, text="C", width=8, height=2, bg="red", fg="white", command=clear_entry).grid(row=5, column=0, columnspan=4, pady=10)

# Run app
root.mainloop()
