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
reps = 0
timer = NONE

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_canvas_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmarks_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec =  SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 ==0:
        count_down(short_break_sec)
        status = "Break"
        timer_label.config(text=f"{status}", fg=PINK)
    elif reps % 8 ==0:
        count_down(long_break_sec)
        status = "Break"
        timer_label.config(text=f"{status}", fg=RED)
    else:
        count_down(work_sec)
        status = "Working"
        timer_label.config(text=f"{status}", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Changing the text on Canvas
    canvas.itemconfig(timer_canvas_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)

    else:
        start_timer()
        marks = "🗸"
        num_of_work_sessions_finished = int(reps/2)
        if reps % 2 ==0:
            checkmarks_label.config(text=f"{marks * num_of_work_sessions_finished}", font=(FONT_NAME, 30, "bold"))

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font= (FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", font=(FONT_NAME, 32, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start",
                      bg="white",
                      highlightthickness=5,
                      command= start_timer
                      )
start_button.grid(column=0, row=2,)

reset_button = Button(text="Reset",
                      bg="white",
                      highlightthickness=5,
                      command= reset_timer
                      )
reset_button.grid(column=2, row=2)

checkmarks_label = Label(fg=GREEN, bg=YELLOW)
checkmarks_label.grid(column=1, row=3)

window.mainloop()