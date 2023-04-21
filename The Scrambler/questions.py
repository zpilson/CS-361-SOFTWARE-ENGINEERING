from tkinter import *


def choose_a_question(page):
    opMenu = Frame(page)
    ansMenu = Frame(opMenu)

    clicked = StringVar()
    clicked.set("Choose a question")

    options = [
        "Choose a question",
        "Question 1",
        "Question 2",
        "Question 3",
    ]

    drop = OptionMenu(opMenu,
                      clicked,
                      *options,
                      command=lambda selection: answer_the_question(selection, ansMenu))

    drop.pack()
    ansMenu.pack()

    return opMenu


def answer_the_question(selection, ansMenu):
    for widgets in ansMenu.winfo_children():
        widgets.destroy()
    if selection == "Question 1":
        Label(ansMenu, text="Answer 1").pack()
    if selection == "Question 2":
        Label(ansMenu, text="Answer 2").pack()
    if selection == "Question 3":
        Label(ansMenu, text="Answer 3").pack()
