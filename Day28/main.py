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
REPS = 0
CHECKMARK = "✓"
timer = None
START_TIMER = "00:00"

# ---------------------------- TIMER RESET ------------------------------- # 
def Reset():
    window.after_cancel(timer)
    pomodoro_canvas.itemconfig(timer_text, text=START_TIMER)
    text_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global REPS
    REPS = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def Start():
    global REPS
    REPS += 1
    
    if REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        text_label.config(text="Break", fg=RED)
    elif REPS % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        text_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        text_label.config(text="Break", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    pomodoro_canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        Start()
        mark = ""
        for _ in range(math.floor(REPS/2)):
            mark += CHECKMARK
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


pomodoro_canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_photo = PhotoImage(file="tomato.png")
pomodoro_canvas.create_image(100, 112, image=pomodoro_photo)
timer_text = pomodoro_canvas.create_text(100, 130, text=START_TIMER, fill="white", font=(FONT_NAME, 35, "bold"))
pomodoro_canvas.grid(row=2, column=2)

start_button = Button(text="Start", command=Start, highlightthickness=0)
start_button.grid(row=4, column=0)

reset_button = Button(text="Reset", command=Reset, highlightthickness=0)
reset_button.grid(row=4, column=4)

text_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
text_label.grid(row=0, column=2)

check_marks = Label(text="✓", fg=GREEN, bg=YELLOW)
check_marks.grid(column=2, row=4)

window.mainloop()