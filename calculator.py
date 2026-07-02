import tkinter as tk
from tkinter import messagebox

history_file = "history.txt"

# -------- FILE FUNCTIONS --------
def save_to_history(equation, result):
    with open(history_file, "a") as file:
        file.write(equation + "=" + str(result) + "\n")

def show_history():
    try:
        with open(history_file, "r") as file:
            lines = file.readlines()
            
        if len(lines) == 0:
            messagebox.showinfo("History", "No history found!")
        else:
            history_text = "".join(reversed(lines))
            messagebox.showinfo("History", history_text)
    except FileNotFoundError:
        messagebox.showinfo("History", "No history file found!")

def clear_history():
    with open(history_file, "w") as file:
        pass
    messagebox.showinfo("History", "History cleared!")

# -------- CALCULATOR FUNCTION --------
def calculate():
    user_input = entry.get()
    
    try:
        parts = user_input.split()
        if len(parts) != 3:
            messagebox.showerror("Error", "Use format: 8 + 8")
            return
        
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
        
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by 0")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operator")
            return
        
        if int(result) == result:
            result = int(result)
        
        result_label.config(text=f"Result: {result}")
        save_to_history(user_input, result)
    
    except ValueError:
        messagebox.showerror("Error", "Invalid input!")

# -------- GUI SETUP --------
root = tk.Tk()
root.title("Simple GUI Calculator")
root.geometry("350x300")
root.resizable(False, False)

# Title
title = tk.Label(root, text="Simple Calculator", font=("Arial", 16))
title.pack(pady=10)

# Entry box
entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

calc_btn = tk.Button(btn_frame, text="Calculate", command=calculate, width=15)
calc_btn.grid(row=0, column=0, padx=5, pady=5)

history_btn = tk.Button(btn_frame, text="Show History", command=show_history, width=15)
history_btn.grid(row=1, column=0, padx=5, pady=5)

clear_btn = tk.Button(btn_frame, text="Clear History", command=clear_history, width=15)
clear_btn.grid(row=2, column=0, padx=5, pady=5)

exit_btn = tk.Button(btn_frame, text="Exit", command=root.quit, width=15)
exit_btn.grid(row=3, column=0, padx=5, pady=5)

# Instruction
instruction = tk.Label(root, text="Enter like: 8 + 8", font=("Arial", 10))
instruction.pack(pady=5)

# Run app
root.mainloop()
        

    