import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = list(string.ascii_letters)
    numbers = list(string.octdigits)
    symbols = list(string.punctuation)

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = password_list + [random.choice(letters) for char in range(nr_letters)]
    password_list = password_list + [random.choice(symbols) for sym in range(nr_symbols)]
    password_list = password_list + [random.choice(numbers) for num in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    input_pass.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = input_website.get()
    email = input_email.get()
    password = input_pass.get()
    saved_entry = f"{website} | {email} | {password} \n"
    if not (website and email and password):
        messagebox.showwarning(title="Empty field", message="Please fill in all fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"The info that you entered for the above website is: "
                                                              f"\nEmail: {email}"
                                                              f"\nPassword: {password}"
                                                              f"\nAre you sure you want to save?")
        if is_ok:
            with open('data.txt', 'a') as f:
                f.write(saved_entry)
                input_pass.delete(0, 'end')
                input_website.delete(0, 'end')



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
btn_add = tk.Button(text="Add", highlightthickness=0, width=44, command=save_password)
btn_gen_pass = tk.Button(text="Generate Password", highlightthickness=0, command=generate_pass)

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
input_website.focus()
input_email = tk.Entry(width=52)
input_email.insert(0, "example@gmail.com")
input_pass = tk.Entry(width=34)

input_website.grid(row=1, column=1, columnspan=2)
input_email.grid(row=2, column=1, columnspan=2)
input_pass.grid(row=3, column=1)
window.mainloop()
