import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)
window.minsize(width=400, height=300)

canvas = tk.Canvas(width=200, height=200)
img_lock = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img_lock)
canvas.grid(row=0, column=1)

# Button
btn_add = tk.Button(text="Add", highlightthickness=0, width=44)
btn_gen_pass = tk.Button(text="Generate Password", highlightthickness=0)

btn_add.grid(row=4, column=1, columnspan=2)
btn_gen_pass.grid(row=3, column=2)

# Label
l_email = tk.Label(text="Email/Username:")
l_website = tk.Label(text="Website:")
l_password = tk.Label(text="Password:")

l_website.grid(row=1, column=0)
l_email.grid(row=2, column=0)
l_password.grid(row=3, column=0)


# Entries
input_website = tk.Entry(width=52)
input_email = tk.Entry(width=52)
input_pass = tk.Entry(width=34)

input_website.grid(row=1, column=1, columnspan=2)
input_email.grid(row=2, column=1, columnspan=2)
input_pass.grid(row=3, column=1)
window.mainloop()
