from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="029-PasswordManager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website label, website entry (width:35)
username_label = Label(text="Website:")
username_label.grid(row=1, column=0)

username_entry = Entry(width=35)
username_entry.grid(row=1, column=1, columnspan=2)

# Email/Username label, email/username entry (width: 35)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)

# Password label, password entry (width: 21), generate button
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=26)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate Password")
password_button.grid(row=3, column=2)

# Add button (width: 35)



window.mainloop()
