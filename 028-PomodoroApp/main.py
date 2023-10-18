from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SEC_PER_MIN = 60
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    title.config(text="Timer", bg=YELLOW, fg=GREEN, )
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * SEC_PER_MIN
    short_seconds = SHORT_BREAK_MIN * SEC_PER_MIN
    long_seconds = LONG_BREAK_MIN * SEC_PER_MIN

    if reps % 8 == 0:
        title.config(text="Break", fg=GREEN)
        countdown(long_seconds)
    elif reps % 2 == 0:
        title.config(text="Break", fg=PINK)
        countdown(short_seconds)
    else:
        title.config(text="Work", fg=RED)
        countdown(work_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    # Format timer into a legible layout
    minutes = math.floor(count / 60)
    seconds = math.floor(count % 60)

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds:02d}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        checks = ""
        for x in range(math.floor(reps / 2)):
            checks += "✔"
        check_marks.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)
window.title("Pomodoro")

# Main Title
title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
title.grid(column=1, row=0)

# Start Button
start_btn = Button(text="Start", command=start_timer, highlightthickness=0)
start_btn.grid(column=0, row=2)

# Reset Button
reset_btn = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_btn.grid(column=2, row=2)

# Check marks
check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15))
check_marks.grid(column=1, row=3)

# Tomato Image and Timer
canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_img = PhotoImage(file="028-PomodoroApp/tomato.png")
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
