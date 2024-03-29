import tkinter as tk
import pandas as pd
import json
import random



# Static Globals
BACKGROUND_COLOR = "#B1DDC6"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"
LANGUAGE_FONT_SIZE = 40
VERB_FONT_SIZE = 60



# Dynamic Globals
# 0 means Greek, 1 means English
word_index = 0
language_index = 0
canvas_side = 0 
language_dictionary = {}

# Display Setup
window = tk.Tk()
window.title("Flashy")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)

## Image Importing
front_card = tk.PhotoImage(file="images/card_front.png")
back_card = tk.PhotoImage(file="images/card_back.png")
r_btn = tk.PhotoImage(file="images/right.png")
w_btn = tk.PhotoImage(file="images/wrong.png")

CARD_STATE = {
    0:{"language":"greek","card_side":front_card},
    1:{"language":"english","card_side":back_card}
}

## Canvas Setup
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)
card_background = canvas.create_image(400,263,image=front_card)
language_text = canvas.create_text(400,150,font=(FONT_NAME,LANGUAGE_FONT_SIZE,"italic"))
vocab_text = canvas.create_text(400,263,font=(FONT_NAME,VERB_FONT_SIZE,"bold"))

# Reading Data Files
def get_list():
    global language_dictionary
    top_words_k = {}
    try:
        with open("data/greek_10k.json", "r") as data_file:
            top_words_k = json.load(data_file)
    except FileNotFoundError:
        full_word_list = pd.read_csv("data/greek_words.csv")
        for i in full_word_list.index:
            if i > 999:
                break
            top_words_k[i] ={
                "english":full_word_list["english"][i],
                "greek":full_word_list["greek"][i],
                "has_learned":False
            }

        with open("data/greek_10k.json", "w") as data_file:
            json.dump(top_words_k, data_file, indent=4)
    
    finally:
        language_dictionary = top_words_k

# Generating Card Words
def get_word():
    global language_dictionary
    global word_index
    #[key for key in top_words.keys() if not top_words[key]["has_learned"]]
    possible_choices = [key for key in language_dictionary.keys() if not language_dictionary[key]["has_learned"]]
    word_index = random.choice(possible_choices)

# Canvas Word Fill   

def update_card():
    global canvas_side
    global card_background
    global language_text
    global vocab_text
    global word_index
    
    canvas.itemconfig(card_background,image=CARD_STATE[canvas_side]["card_side"])
    canvas.itemconfig(language_text, text=(CARD_STATE[canvas_side]["language"]).capitalize())
    canvas.itemconfig(vocab_text, text=language_dictionary[word_index][CARD_STATE[canvas_side]["language"]])
    
def card_flip(event):
    global canvas_side
    if canvas_side == 0:
        canvas_side = 1
    else:
        canvas_side = 0
    
    update_card()

# Button Methods
def new_word():
    global canvas_side
    get_word()
    if canvas_side == 1:
        canvas_side = 0
    update_card()

def right_button():
    global word_index
    global language_dictionary
    language_dictionary[word_index]["has_learned"] = True
    new_word()

# Save Progress ON QUIT
def save_progress():
    global language_dictionary
    with open("data/greek_10k.json", "w") as data_file:
        json.dump(language_dictionary,data_file,indent=4)

    window.destroy()
    

# Button Setup
right_btn = tk.Button(image=r_btn, highlightthickness=0, command=right_button)
wrong_btn = tk.Button(image=w_btn, highlightthickness=0, command=new_word)
right_btn.grid(row=1,column=1)
wrong_btn.grid(row=1,column=0)

canvas.bind("<Button-1>", card_flip)

get_list()
get_word()
update_card()
window.protocol("WM_DELETE_WINDOW", save_progress)
window.mainloop()