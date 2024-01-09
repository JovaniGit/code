from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

card = {}


def yes_button():
    word_dic.remove(card)
    create_card()
    new_data = pandas.DataFrame(word_dic)
    new_data.to_csv('words_to_learn.csv')


def create_card():
    global card, flip_time
    screen.after_cancel(flip_time)
    card = random.choice(word_dic)
    canvas.itemconfigure(word, text=card['French'])
    canvas.itemconfigure(title, text='French')
    canvas.itemconfigure(front_card, image=img_f)
    flip_time = screen.after(3000, change)


def change():
    canvas.itemconfigure(word, text=card['English'])
    canvas.itemconfigure(title, text='English')
    canvas.itemconfigure(front_card, image=img_b)


try:
    data = pandas.read_csv('words_to_learn.csv')

except FileNotFoundError:
    data = pandas.read_csv('french_words.csv')
    word_dic = data.to_dict(orient="records")

else:
    word_dic = data.to_dict(orient="records")

screen = Tk()
screen.title('Flash Card Program')
screen.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_time = screen.after(3000, change)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_f = PhotoImage(file='images/card_front.png')
front_card = canvas.create_image(400, 265)
img_b = PhotoImage(file='images/card_back.png')
title = canvas.create_text(400, 200, font=("Courier", 30, "italic"))
word = canvas.create_text(400, 300, font=("Ariel", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

y_img = PhotoImage(file='images\\right.png')
y_button = Button(image=y_img, highlightthickness=0, command=yes_button)
y_button.grid(column=0, row=1)

n_img = PhotoImage(file='images\\wrong.png')
n_button = Button(image=n_img, highlightthickness=0, command=create_card)
n_button.grid(column=1, row=1)

create_card()

screen.mainloop()
