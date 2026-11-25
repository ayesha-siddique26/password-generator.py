import tkinter as tk
import random
import string

def generate():
    try:
        length = int(length_entry.get())
    except:
        length = 12
    
    if length < 4:
        length = 4
    if length > 30:
        length = 30

    chars = ""
    if var_upper.get():
        chars += string.ascii_uppercase
    if var_lower.get():
        chars += string.ascii_lowercase
    if var_digits.get():
        chars += string.digits
    if var_symbols.get():
        chars += string.punctuation

    if chars == "":
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Koi option select karo!")
        return

    password = "".join(random.choice(chars) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

def copy_pass():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    copy_btn.config(text="Copied! ✅")
    root.after(1000, lambda: copy_btn.config(text="Copy Karo"))

root = tk.Tk()
root.title("Ayesha's Password Generator")
root.geometry("400x450")
root.configure(bg="#1a1a2e")

title = tk.Label(root, text="🔐 Password Generator", font=("Arial", 20, "bold"), bg="#1a1a2e", fg="white")
title.pack(pady=15)

# Length
tk.Label(root, text="Kitne letters ka password chahiye?", font=("Arial", 12), bg="#1a1a2e", fg="white").pack()
length_entry = tk.Entry(root, font=("Arial", 16), justify="center", width=10)
length_entry.insert(0, "12")
length_entry.pack(pady=5)

# Options
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="ABC  (Bare Letters)", variable=var_upper, bg="#1a1a2e", fg="white", selectcolor="#1a1a2e", font=("Arial", 12)).pack(anchor="w", padx=80)
tk.Checkbutton(root, text="abc  (Chote Letters)", variable=var_lower, bg="#1a1a2e", fg="white", selectcolor="#1a1a2e", font=("Arial", 12)).pack(anchor="w", padx=80)
tk.Checkbutton(root, text="123  (Numbers)", variable=var_digits, bg="#1a1a2e", fg="white", selectcolor="#1a1a2e", font=("Arial", 12)).pack(anchor="w", padx=80)
tk.Checkbutton(root, text="@#$  (Symbols)", variable=var_symbols, bg="#1a1a2e", fg="white", selectcolor="#1a1a2e", font=("Arial", 12)).pack(anchor="w", padx=80)

gen_btn = tk.Button(root, text="Generate Karo ✨", font=("Arial", 14, "bold"), bg="#e94560", fg="white", width=20, command=generate)
gen_btn.pack(pady=15)

result_entry = tk.Entry(root, font=("Arial", 14), justify="center", width=30)
result_entry.pack(pady=5)

copy_btn = tk.Button(root, text="Copy Karo", font=("Arial", 12), bg="#0f3460", fg="white", width=15, command=copy_pass)
copy_btn.pack(pady=10)

root.mainloop()
