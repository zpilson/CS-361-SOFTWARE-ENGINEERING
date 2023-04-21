from tkinter import *


def enter_code(page):
    enterCodeFrame = Frame(page)

    myEntry = Entry(enterCodeFrame)
    myEntry.insert(0, "Enter Code...")
    myEntry.pack(side=LEFT)

    Button(enterCodeFrame, text="Submit").pack(side=LEFT)    # add a command that takes user-input as a param

    return enterCodeFrame



