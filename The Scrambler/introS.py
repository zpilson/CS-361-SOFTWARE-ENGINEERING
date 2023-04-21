from tkinter import *

def intro_for_scrambler(page):
    title_and_intro = Frame(page)

    scramblerTitle = Label(                             # Title Header
        title_and_intro,
        text="SCRAMBLER",
        font=("Modern", 45, "underline", "bold"))

    scramblerIntroduction = Label(                      # Intro/Description
        title_and_intro,
        text="Welcome to the scrambler! \n"
             "Enter text in the text box below "
             "and once you are finished, \n"
             "press the scrambled button to "
             "see your results. \n\n"
             "In order for text to be scrambled "
             "to your liking, \n"
             "please select some of the given "
             "options available \n"
             "on the right side of the "
             "textbox.\n ")

    scramblerTitle.pack()                               # adds title to frame
    scramblerIntroduction.pack()                        # adds intro to frame

    return title_and_intro                              # Returns a Frame: Title + Intro