from tkinter import *

window = Tk()
window.title("M>KM")
window.minsize(200, 1)
window.config(padx=20, pady=20)


def convert():
    km = int(user_entry.get()) * 1.6
    km_result_label.config(text=km)


# Row 1: null, user_entry, miles_label
# Row 2: miles_result_label, result_label, label
# Row 3: null, button, null

# Row 0
user_entry = Entry(width=10)
user_entry.insert(END, string="0")
user_entry.grid(column=1, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

# Row 1
text_label = Label(text="is equal to")
text_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

# Row 2
convert_button = Button(text="Convert", command=convert)
convert_button.grid(column=1, row=2)


window.mainloop()
