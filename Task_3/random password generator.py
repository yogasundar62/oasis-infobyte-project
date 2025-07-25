import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip
def generate_password(length, use_letters, use_digits, use_symbols):
    char_pool = ''
    if use_letters:
        char_pool += string.ascii_letters
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation
    if not char_pool:
        return None  
    return ''.join(random.choice(char_pool) for _ in range(length))
def gui_mode():
    def on_generate():
        length = length_var.get()
        use_letters = letters_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()
        password = generate_password(length, use_letters, use_digits, use_symbols)
        if password:
            password_var.set(password)
        else:
            messagebox.showerror("Error", "Please select at least one character type.")
    def copy_to_clipboard():
        pw = password_var.get()
        if pw:
            pyperclip.copy(pw)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
    win = tk.Tk()
    win.title(" Random Password Generator")
    win.geometry("350x300")
    win.resizable(False, False)
    tk.Label(win, text="Password Length:", font=('Arial', 10)).grid(row=0, column=0, sticky='w', padx=10, pady=10)
    length_var = tk.IntVar(value=12)
    tk.Scale(win, from_=4, to=64, variable=length_var, orient="horizontal", length=200).grid(row=0, column=1, padx=10)
    letters_var = tk.BooleanVar(value=True)
    digits_var = tk.BooleanVar(value=True)
    symbols_var = tk.BooleanVar(value=True)
    tk.Checkbutton(win, text="Include Letters", variable=letters_var).grid(row=1, column=0, columnspan=2, sticky='w', padx=10)
    tk.Checkbutton(win, text="Include Digits", variable=digits_var).grid(row=2, column=0, columnspan=2, sticky='w', padx=10)
    tk.Checkbutton(win, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, columnspan=2, sticky='w', padx=10)
    tk.Button(win, text=" Generate Password", command=on_generate, bg="#4CAF50", fg="white", padx=10).grid(row=4, column=0, columnspan=2, pady=15)
    password_var = tk.StringVar()
    tk.Entry(win, textvariable=password_var, width=30, font=('Arial', 12)).grid(row=5, column=0, columnspan=2, padx=10, pady=5)
    tk.Button(win, text=" Copy to Clipboard", command=copy_to_clipboard).grid(row=6, column=0, columnspan=2, pady=10)
    win.mainloop()
gui_mode()


 
