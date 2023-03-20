import time
from tkinter import Tk, PhotoImage, Canvas, Button
from word_pick import Word
#__________________________backend_____________________________________


def time_card():
    pass
def answer():
    cback()
    canvas.itemconfig(language, text="English", fill="black")
    canvas.itemconfig(text, text=word.word_in_english, fill="black")
def newword():
    cfront()
    canvas.itemconfig(language, text="French", fill="white")
    canvas.itemconfig(text, text=word.word_in_french, fill="white")
    canvas.after(4000, answer)
def rightpass():
    word.right()
    newword()

def wrongpass():
    word.wrong()
    newword()




#_______________________UI_________________________________________
def btright(e):
    rt["image"] = rightoff
def obtright(e):
    rt["image"] = right
def btwrong(e):
    wg["image"] = wrongoff
def obwrong(e):
    wg["image"] = wrong
def cfront():
    canvas.itemconfig(card, image=front_card)
def cback():
    canvas.itemconfig(card, image=back_card)
home = Tk()

home.title("Flash Card")
word = Word()
home.geometry("447x335")
bg = PhotoImage(file="image/backgroundldpi.png")
front_card = PhotoImage(file="image/wordldpi.png")
back_card = PhotoImage(file="image/answerldpi.png")
wrong = PhotoImage(file="image/wrongldpi.png")
right = PhotoImage(file="image/rightldpi.png")
wrongoff = PhotoImage(file="image/wrongoffldpi.png")
rightoff = PhotoImage(file="image/rightoffldpi.png")
canvas = Canvas(width=448,height=336)
canvas.create_image(224,168, image=bg)
card = canvas.create_image(224,168, image=front_card)
language =  canvas.create_text(224, 108, text="French", font=("Space Quest", 20, "italic"), fill="white")
text = canvas.create_text(224, 168, text=word.word_in_french, font=("Space Quest", 35), fill="white")
rt = Button(image=right, border=0, bg="#24126a", command=rightpass)
rt.place(x=70, y=285)
rt.bind("<Enter>", btright)
rt.bind("<Leave>", obtright)
wg = Button(image=wrong, border=0, bg="#24126a", command=wrongpass)
wg.place(x=320, y=285)
wg.bind("<Enter>", btwrong)
wg.bind("<Leave>", obwrong)
home.after(4000, answer)
canvas.place(x=-2, y=-2)
home.mainloop()