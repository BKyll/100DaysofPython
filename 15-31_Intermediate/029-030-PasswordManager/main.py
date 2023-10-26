from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }
    if "" not in {website_entry.get(), username_entry.get(), password_entry.get()}:
        try:
            with open("passwords.json", "r") as password_file:
                # Read old data
                data = json.load(password_file)
                # Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally:
            with open("passwords.json", "w") as password_file:
                # Saving updated data
                json.dump(data, password_file, indent=4)

            clear_form()
    else:
        messagebox.showerror(title="Incomplete Information", message="Please fill all data fields.")


def clear_form():
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    username_entry.insert(0, "bryan@email.com")
    password_entry.delete(0, END)


def search_password():
    try:
        site = website_entry.get()
        with open("passwords.json", 'r') as password_file:
            data = json.load(password_file)
            email = data[site]["email"]
            password = data[site]["password"]
            messagebox.showinfo(title=site, message=f"Email: {email}\nPassword: {password}")
    except FileNotFoundError:
        messagebox.showinfo(title="File not found", message=f"No password file found.")
    except KeyError:
        messagebox.showinfo(title="Entry not found", message=f"No details for '{site}' found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website label, website entry (width:35)
website_label = Label(text="Website:", width=15, anchor='e')
website_label.grid(row=1, column=0, sticky='e')

website_entry = Entry(width=32)
website_entry.grid(row=1, column=1, columnspan=2, sticky='w')
website_entry.focus()

website_button = Button(text="Search", command=search_password, width=13)
website_button.grid(row=1, column=2, sticky='w')

# Email/Username label, email/username entry (width: 35)
username_label = Label(text="Email/Username:", width=15, anchor='e')
username_label.grid(row=2, column=0, sticky='e')

username_entry = Entry(width=50)
username_entry.grid(row=2, column=1, columnspan=2, sticky='w')
username_entry.insert(0, "bryan@email.com")

# Password label, password entry (width: 21), generate button
password_label = Label(text="Password:", width=15, anchor='e')
password_label.grid(row=3, column=0, sticky='e')

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1, sticky='w')

password_button = Button(text="Generate", command=generate_password, width=13)
password_button.grid(row=3, column=2, sticky='w')

# Add button (width: 35)
add_button = Button(text="Add", width=42, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky='w')

window.mainloop()
