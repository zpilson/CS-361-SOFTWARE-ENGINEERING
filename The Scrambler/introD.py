from tkinter import *

def intro_for_decipher(page):
    title_and_intro = Frame(page)

    decipherTitle = Label(                             # Title Header
        title_and_intro,
        text="Decipher",
        font=("Modern", 45, "underline", "bold"))

    decipherIntroduction = Label(                      # Intro/Description
        title_and_intro,
        text="Welcome to the decipher! \n"
             "Please copy and paste your encoded \n"
             "message that was created from the \n"
             "scrambler into the text box below. \n\n"
             "In the bottom right corner, provide \n"
             "the code given to you after scrambling \n"
             "your text to properly decipher your message. \n\n"
             "Once done, press the decipher\n"
             "button to decode your message.\n" )

    decipherTitle.pack()                               # adds title to frame
    decipherIntroduction.pack()                        # adds intro to frame

    return title_and_intro                             # Returns a Frame: Title + Intro