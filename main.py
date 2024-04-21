
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
BLUE = "#74CFCF" 
BLACK = "#070F2B"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_to_cancel = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    window.after_cancel(timer_to_cancel)
    canvas.itemconfig(timer, text="00:00")
    timer_text.config(text="Timer")
    tick.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(short_break_sec)
        timer_text.config(text="Short Break")
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_text.config(text="Long Break")
    else:
        timer_text.config(text="Work Timer")
        count_down(work_sec)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # for i in range(1, 10):
    #     if count_sec == i:
    #         count_sec = "0" + str(count_sec)
    #     elif count_sec == 0:
    #         count_sec = "00"

    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_to_cancel
        timer_to_cancel = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        tick.config(text=mark)




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=BLUE)


canvas = Canvas(width="200", height="224", bg=BLUE, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png") # requires file path, enables to put image inside create_image function
canvas.create_image(100, 112, image=tomato_img) # x, y positions are required
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

timer_text = Label(text="Timer", font=(FONT_NAME, 50), fg=BLACK, bg=BLUE)
timer_text.grid(column=2, row=1)

button = Button(text="Start", padx=7, pady=5, command=start_timer)
button.grid(column=1, row=3)

button = Button(text="Reset", padx=7, pady=5, command=reset)
button.grid(column=3, row=3)

tick = Label(fg=BLACK, bg=BLUE)
tick.grid(column=2, row=4)



window.mainloop()