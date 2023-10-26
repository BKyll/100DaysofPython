from tkinter import *

window = Tk()
window.title("TKinter GUI")
window.minsize(500, 300)
window.config(padx=20, pady=20)

# Label
label = Label(text="Label!", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)
# label["text"] = "New Text"
label.config(text="Don't click \nthe button!", padx=50, pady=50)


# Button
def button_clicked():
    label.config(text=entry.get())


def button_clear():
    label.config(text="Don't click \nthe button!")


button = Button(text="Click me!", command=button_clicked)
button.grid(column=1, row=1)

button_2 = Button(text="Clear", command=button_clear)
button_2.grid(column=2, row=0)

# Entry
entry = Entry(width=10)
entry.grid(column=4, row=2)

# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total
#
#
# print(add(1, 2, 3, 4, 5, 65, 6, 55, 4, 3, 2, 1))

# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")
#         self.year = kw.get("year")
#
# # my_car = Car(make="Subaru", model="Outback")
# # my_car = Car(make="Ford")
# my_car = Car(make="Subaru", model="Outback", color="grey", year=2020)
# print(f"{my_car.year} {my_car.make} {my_car.model}, {my_car.color}")


window.mainloop()
