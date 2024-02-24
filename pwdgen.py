import random
import string
import tkinter as tk
from tkinter import messagebox

import pyperclip


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer")
        password = generate_password(length)
        txt_generated_password.config(state=tk.NORMAL)
        txt_generated_password.delete(1.0, tk.END)
        txt_generated_password.insert(tk.END, password)
        txt_generated_password.config(state=tk.DISABLED)
    except ValueError as ve:
        messagebox.showerror("Error", "Invalid input: " + str(ve))

def copy_password():
    password = txt_generated_password.get(1.0, tk.END).strip()
    pyperclip.copy(password)
    messagebox.showinfo("Info", "Password copied to clipboard")


def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#333333")

# Create a frame for user input
frame_input = tk.Frame(root, bg="#333333")
frame_input.grid(row=0, column=0, padx=10, pady=10)

# Create a label and entry widget for password length input
lbl_length = tk.Label(frame_input, text="Password Length:", bg="#333333", fg="white")
lbl_length.grid(row=0, column=0, padx=(0, 10))
entry_length = tk.Entry(frame_input, width=10)
entry_length.grid(row=0, column=1)

# Create a button to generate password
btn_generate = tk.Button(frame_input, text="Generate", command=generate, bg="#555555", fg="white", activebackground="#777777", activeforeground="white")
btn_generate.grid(row=0, column=2, padx=(10, 5))

# Create a button to copy password
btn_copy = tk.Button(frame_input, text="Copy", command=copy_password, bg="#555555", fg="white", activebackground="#777777", activeforeground="white")
btn_copy.grid(row=0, column=3)

# Create a frame for displaying generated password
frame_output = tk.Frame(root, bg="#333333")
frame_output.grid(row=1, column=0, padx=10, pady=10)

# Create a label for displaying generated password
lbl_generated_password = tk.Label(frame_output, text="Generated Password:", bg="#333333", fg="white")
lbl_generated_password.grid(row=0, column=0, pady=(0, 5))

# Create a scrolled text widget for displaying generated password
txt_generated_password = tk.Text(frame_output, width=40, height=3, bg="#555555", fg="white")
txt_generated_password.grid(row=1, column=0)
txt_generated_password.config(state=tk.DISABLED)

# Create a button to exit the application
btn_exit = tk.Button(root, text="Exit", command=exit_app, bg="#555555", fg="white", activebackground="#777777", activeforeground="white")
btn_exit.grid(row=2, column=0, pady=(0, 10))

# Start the GUI event loop
root.mainloop()
