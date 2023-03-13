import tkinter as tk
from tkinter import messagebox
import json
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
    saved_entry = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if not (website and email and password):
        messagebox.showwarning(title="Empty field", message="Please fill in all fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"The info that you entered for the above website is: "
                                                              f"\nEmail: {email}"
                                                              f"\nPassword: {password}"
                                                              f"\nAre you sure you want to save?")
        if is_ok:
            try:
                with open('data.json', 'r') as f:
                    data = json.load(f)
            except FileNotFoundError:
                with open("data.json", "w") as f:
                    json.dump(saved_entry, f, indent=4)
            else:
                data.update(saved_entry)
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)
            finally:
                input_pass.delete(0, 'end')
                input_website.delete(0, 'end')

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_pass_for_web():
    website_name = input_website.get()
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showwarning(title="File Not Found", message="Could not find the data file")
    else:
        retrieved_web_dict = data.get(website_name, None)
        if retrieved_web_dict:
            messagebox.showinfo(title="Password Found", message=f"The password for your website is: \n {retrieved_web_dict['password']}")
            pyperclip.copy(retrieved_web_dict['password'])
        else:
            messagebox.showwarning(title="No password found", message="Could not find the website you are looking for in our database")


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
btn_search = tk.Button(text="Search", highlightthickness=0, width=14, command=search_pass_for_web)

btn_add.grid(row=4, column=1, columnspan=2)
btn_gen_pass.grid(row=3, column=2)
btn_search.grid(row=1, column=2)

# Label
l_email = tk.Label(text="Email/Username:")
l_website = tk.Label(text="Website:")
l_password = tk.Label(text="Password:")

l_website.grid(row=1, column=0)
l_email.grid(row=2, column=0)
l_password.grid(row=3, column=0)


# Entries
input_website = tk.Entry(width=34)
input_website.focus()
input_email = tk.Entry(width=52)
input_email.insert(0, "example@gmail.com")
input_pass = tk.Entry(width=34)

input_website.grid(row=1, column=1)
input_email.grid(row=2, column=1, columnspan=2)
input_pass.grid(row=3, column=1)
window.mainloop()
