from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.configure(padx=50, pady=50, background=BACKGROUND_COLOR)
window.title("Flash Cards")

card_f = PhotoImage(file="images/card_front.png")
card_b = PhotoImage(file="images/card_back.png")
button_correct = PhotoImage(file="images/right.png")
button_wrong = PhotoImage(file="images/wrong.png")

canvas = Canvas()
canvas.create_image(100, 100, image=card_f)
canvas.grid(row=0, column=0, columnspan=2)

window.mainloop()
