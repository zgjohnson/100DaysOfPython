from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 2
reps = 0
timer = ''


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    check_label.config(text='')
    timer_label.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    
    work_seconds = WORK_MIN * 1
    short_break_seconds = SHORT_BREAK_MIN * 1
    long_break_seconds = LONG_BREAK_MIN * 1

    if reps % 8 == 0:
        count_down(long_break_seconds)
        timer_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        timer_label.config(text='Break', fg=PINK)
    else:
        count_down(work_seconds)
        timer_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minuet = math.floor(count / 60)
    second = count % 60
    if second < 10:
        second = f'0{second}'
    if minuet < 10:
        minuet = f'0{minuet}'

    canvas.itemconfig(timer_text, text=f'{minuet}:{second}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += '✔'
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(pady=50, padx=100, bg=YELLOW)

timer_label = Label(fg=GREEN, bg=YELLOW, text='Timer', font=(FONT_NAME, 50, 'bold'))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

start_button = Button(text='Start', font=(FONT_NAME, 10, 'normal'), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', font=(FONT_NAME, 10, 'normal'), command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, 'bold'))
check_label.grid(row=3, column=1)

window.mainloop()
