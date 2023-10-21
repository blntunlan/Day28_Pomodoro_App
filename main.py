import tkinter as tk
import time

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
COUNTER = 0
x = 50
y = 350
mola_count = 0

# Function to get the timer length from the entry box
def get_timer_length():
    """Gets the timer length from the entry box."""
    numb = entry_label.get()
    countdown(int(numb) * 60)

# Timer mechanism
def countdown(seconds=1500):
    global COUNTER, mola_count
    countdown.is_on = True
    while seconds > 0 and countdown.is_on:
        canvas.itemconfig(2, text=f"{seconds // 60:02}:{seconds % 60:02}")
        canvas.update()
        time.sleep(1)
        seconds -= 1
        if seconds == 0:
            reset_timer()
            COUNTER += 1
            counter_tik()
            mola()
        if mola_count > 5:
            canvas.itemconfig(2, text="Take a long break")
            canvas.update()
            time.sleep(1)
            seconds = 1200
            mola_count = 0
    return seconds

# Other functions
def counter_tik():
    global x, y, COUNTER
    if COUNTER > 0:
        x += 25
        tik(x, y)
    if COUNTER % 5 == 0:
        x = 50
        y += 25
        tik(x, y)

def mola():
    global mola_count
    mola_count += 1
    countdown(300)

def reset_timer():
    countdown.is_on = False
    canvas.itemconfig(2, text=f"00:00")
    canvas.update()

# Start the timer
def start_timer():
    seconds = get_timer_length()
    countdown(seconds)

def tik(x, y):
    tik_label = tk.Label(text="✔", fg=GREEN, background=YELLOW, font=(FONT_NAME, 15, "bold"))
    tik_label.place(x=x, y=y)

# UI Setup
root = tk.Tk()
root.title("Pomodoro")
root.config(padx=100, pady=50, bg=YELLOW)
root.minsize(width=500, height=500)
root.resizable(width=False, height=False)

canvas = tk.Canvas(width=200, height=224, highlightthickness=0, bg=YELLOW)
timer_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=timer_image, anchor="center", tag="image", state="normal")
canvas.create_text(100, 130, text="00:00", fill="black", font=(FONT_NAME, 45, "bold"))
canvas.place(x=50, y=50)

label = tk.Label(text="Timer", fg=GREEN, background=YELLOW, font=(FONT_NAME, 50, "bold"))
label.place(x=50, y=-60)

entry_label = tk.Entry(width=6, highlightthickness=0, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
entry_label.place(x=100, y=250)

minutes_button = tk.Button(text="Minutes", highlightthickness=0, bg=YELLOW, font=(FONT_NAME, 12, "bold"), command=get_timer_length)
minutes_button.place(x=100, y=285)

start_button = tk.Button(text="Start", highlightthickness=0, bg=YELLOW, font=(FONT_NAME, 15, "bold"), command=countdown)
start_button.place(x=0, y=250)

reset_button = tk.Button(text="Reset", highlightthickness=0, bg=YELLOW, font=(FONT_NAME, 15, "bold"), command=reset_timer)
reset_button.place(x=200, y=250)

root.mainloop()
