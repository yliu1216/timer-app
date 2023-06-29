from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer")
    my_click.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        my_label.config(text="Break", fg=RED)
       # break_label = Label(text="Break", fg=RED, font=("Arial", 35, "bold"))
       # break_label.grid(column=1, row=0)

    elif reps % 2 == 0:
        my_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
        #break_label = Label(text="Break", fg=PINK, font=("Arial", 35, "bold"))
       # break_label.grid(column=1, row=0)

    else:
        my_label.config(text="Timer", fg=GREEN)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import time
# Event Driven
def count_down(count):
    mintue = math.floor(count / 60)
    second = count % 60
    if second < 10:
        second = f"0{second}"
    canvas.itemconfig(timer_text, text=f"{mintue}:{second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        my_click.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=100, padx=50, background=YELLOW)


canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

# label
my_label = Label(text="Timer", fg=GREEN, font=("Arial", 35, "bold"))
my_label.grid(column=1, row=0)

# click
my_click = Label(fg=GREEN, bg=YELLOW, font=FONT_NAME)
my_click.grid(column=1, row=5)

# button
start_button = Button(text="Start", bg="white", fg="black", font=("Arial", 10, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=4)

# reset
reset_button = Button(text="Reset", bg="white", fg="black", font=("Arial", 10, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=4)
window.mainloop()

