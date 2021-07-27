from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
BLUE = "#2f5d62"
DARKBLUE = "#364547"
BEIGE = "#ffe268"
YELLOW = "#FFB037"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=DARKBLUE)
    canvas.itemconfig(time_text, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it is 8 reps
    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text="Break", fg=YELLOW)
    # If it is 2/4/6 rep:
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Break", fg=YELLOW)
    # If it is 1/3/5/7 reps
    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=DARKBLUE)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            mark += "✓"
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BEIGE)

# Canvas
canvas = Canvas(width=200, height=224, bg=BEIGE, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

# Label

title_label = Label(text="Timer", bg=BEIGE, fg=DARKBLUE, font=(FONT_NAME, 36, "bold"))
title_label.grid(column=1, row=0)

check_label = Label(bg=BEIGE, fg=YELLOW, font=(FONT_NAME, 20))
check_label.grid(column=1, row=3)

# Button

start_button = Button(text="Start", bg=BEIGE, fg=BLUE, font=(FONT_NAME, 14), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=BEIGE, fg=BLUE, font=(FONT_NAME, 14), command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
