from random import *
from tkinter import Tk, Canvas, PhotoImage, Button

from pandas import *


def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_word['English'], fill='white')


def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = choice(to_learn)
    canvas.itemconfig(card_title, text='Spanish', fill='black')
    canvas.itemconfig(card_word, text=current_word['Spanish'], fill='black')
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def known_word():
    to_learn.remove(current_word)
    new_words_to_learn = DataFrame(to_learn)
    new_words_to_learn.to_csv('./data/spanish_words_to_learn.csv', index=False)
    next_card()


BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
to_learn = {}

try:
    data = read_csv("./data/spanish_words_to_learn.csv")
except FileNotFoundError:
    original_data = read_csv("./data/spanish_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
card_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text='Spanish', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

check_image = PhotoImage(file='./images/right.png')
known_button = Button(image=check_image, highlightthickness=0, borderwidth=0, command=next_card)
known_button.grid(row=1, column=1)

cross_image = PhotoImage(file='./images/wrong.png')
unknown_button = Button(image=cross_image, highlightthickness=0, borderwidth=0, command=known_word)
unknown_button.grid(row=1, column=0)

flip_timer = window.after(3000, func=flip_card)
next_card()

window.mainloop()
