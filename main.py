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
rep = 0
cycle_rep = ""
timer_window = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global rep
    global cycle_rep
    global timer_window
    rep = 0
    cycle_rep = ""
    check_marks.config(text=cycle_rep)
    canvas.itemconfig(timer_time_text, text="00:00")
    Timer_text.config(text="POMODORO STUDY")
    window.after_cancel(timer_window)


# ---------------------------- TIMER MECHANISM ------------------------------- #
# TODO 25work, 5BREAK, 25work, 5BREAK, 25work, 5BREAK, 25work, 20BREAK
# TODO   1       2      3        4       5       6       7       8


def start_timer():
    print("start timer")
    global cycle_rep
    global rep
    rep += 1
    print("before countdown", rep)
    if rep <= 9:
        if rep == 9:
            cycle_rep = ""
            print(cycle_rep)
            rep = 0
            check_marks.config(text=cycle_rep)
            start_timer()
        elif rep == 8:
            window.attributes('-topmost', True)
            window.attributes('-topmost', False)
            print("BEFORE LAST REP")
            check_marks.config(text=cycle_rep)
            print("AFTER LAST REP", cycle_rep)
            countdown(LONG_BREAK_MIN*60)
            print("25 min break break break break break break break break break break break ")
            canvas.itemconfig(timer_time_text, fill=RED)
            Timer_text.config(text="25 min BREAK")
            canvas.config()


        elif rep % 2 == 1:
            countdown(WORK_MIN*60)
            print("25 min work period work period work period")
            canvas.itemconfig(timer_time_text, fill=PINK)
            Timer_text.config(text="25 min WORK")
            cycle_rep += "✔"


        elif(rep % 2) == 0:
            window.attributes('-topmost', True)
            window.attributes('-topmost', False)
            countdown(SHORT_BREAK_MIN*60)
            print("5 min break period")
            canvas.itemconfig(timer_time_text, fill=GREEN)
            Timer_text.config(text="5 min BREAK")
            check_marks.config(text=cycle_rep)



    print("after countdown")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    count_min = f'{(math.floor(count/60)):02d}'
    count_sec = f'{(count % 60):02d}'
    # count_sec = f'{count_sec:02d}' #makes it so that it will always have 2 decimal places.
    fin_count = f"{count_min}:{count_sec}"

    if count > 0:
        canvas.itemconfig(timer_time_text, text=f"{fin_count}")
        global timer_window
        timer_window = window.after(1000, countdown, count-1)
        # print(canvas.itemcget(timer_time_text, 'text')) #this is how you get the property of a object on the canvas.
        print(fin_count)

    if count == 0:
        start_timer()
        print(fin_count)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro study technique")
window.config(padx=100, pady=50, bg=PINK)

#use fg = COLOR for what i want my text color to be if i make a Label.

canvas = Canvas(width=215, height=230, bg=PINK, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(110, 112, image=tomato_image)
#
Start_text = Button(text="Start", font=(FONT_NAME, 20, "bold"), bg=GREEN, command=start_timer)
Start_text.grid(column=1, row=3)

Reset_text = Button(text="Reset", font=(FONT_NAME, 20, "bold"), bg=RED, command=reset_timer)
Reset_text.grid(column=3, row=3)

check_marks = Label(text="", bg=PINK, fg=GREEN, font=(FONT_NAME, 40, "bold"))
check_marks.grid(column=2, row=4)


canvas.grid(column=2, row=2)
Timer_text = Label(text="POMODORO STUDY", font=(FONT_NAME, 40, "bold"), bg=PINK)
Timer_text.grid(column=2, row=1)
timer_time_text = canvas.create_text(110, 130, text="00:00", fill="white", font=(FONT_NAME, 22, "bold"))

import time
# count = 10
# while True:
#     time.sleep(1)
#     count -= 1
#     print(count)


# check_image = PhotoImage(file="checkmark-symbol-png-background-12.png")
# check1 = canvas.create_image(110, 112, image=check_image,)
# check1.grid(column=2, row=4)


window.mainloop()
























































