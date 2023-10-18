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
canvas.grid(column=0, row=0)

window.mainloop()
