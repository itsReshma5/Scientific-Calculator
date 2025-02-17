import tkinter as tk
from tkinter import messagebox
import math

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            entry_var.set("")
    elif text == "C":
        entry_var.set("")
    elif text == "√":
        try:
            result = math.sqrt(float(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            entry_var.set("")
    elif text == "^":
        entry_var.set(entry_var.get() + "**")
    else:
        entry_var.set(entry_var.get() + text)

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x500")
root.configure(bg="#2c3e50")

tk.Label(root, text="Scientific Calculator", font="Arial 18 bold", bg="#2c3e50", fg="white").pack()

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", justify="right", bd=10, relief=tk.RIDGE, bg="#ecf0f1")
entry.pack(fill=tk.X, padx=10, pady=10)

button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    [".", "√", "^", "%"]
]

for row in buttons:
    frame = tk.Frame(button_frame, bg="#2c3e50")
    frame.pack()
    for btn in row:
        button = tk.Button(frame, text=btn, font="Arial 15", width=6, height=2, bg="#34495e", fg="white", relief=tk.GROOVE)
        button.pack(side=tk.LEFT, padx=5, pady=5)
        button.bind("<Button-1>", on_click)

root.mainloop()
