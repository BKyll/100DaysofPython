from tkinter import *
import random

import pandas
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

words_df = {}
word = {}

try:
    words_df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words_df = pd.read_csv("data/spanish_words.csv")
finally:
    words_to_learn = words_df.to_dict(orient='records')


def pick_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(words_to_learn)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(language_label, text="Spanish", fill="black")
    canvas.itemconfig(word_label, text=word["Spanish"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global word
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=word["English"], fill="white")


def known_word():
    words_to_learn.remove(word)
    print(len(words_to_learn))
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    pick_word()


# Main window
# # Window creation
window = Tk()
window.configure(padx=50, pady=50, background=BACKGROUND_COLOR)
window.title("Flash Cards: Spanish")
flip_timer = window.after(3000, flip_card)

# # Images
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
correct_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# # Canvas creation
canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.config(background=BACKGROUND_COLOR)

canvas_image = canvas.create_image(400, 263, image=card_front)
language_label = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_label = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

correct_button = Button(image=correct_image, highlightthickness=0, command=known_word)
correct_button.grid(row=1, column=0)

wrong_button = Button(image=wrong_image, highlightthickness=0, command=pick_word)
wrong_button.grid(row=1, column=1)

# Main
pick_word()

window.mainloop()
