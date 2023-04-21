from tkinter import *
from introS import intro_for_scrambler
from introD import intro_for_decipher
from questions import choose_a_question
from TextBox import submit_text
from options import options
from decipherCode import enter_code


def main():
    root = Tk()                     # Birth of a page
    root.title("The Scrambler")

    page = Frame(root)              # Base Case: Starts on scrambler page, button navigates to decipher page
    page.pack()
    Button(
        page,
        text="Decipher Page",
        command=lambda: managePage(page, root, "d")).pack()
    scrambler(page)

    page.mainloop()                 # Infinitely looping the page


def managePage(page, root, s_d):
    if s_d == "d":                  # Button will now navigate to Decipher Page
        page.destroy()
        page = Frame(root)
        page.pack()
        Button(
            page,
            text="Scrambler Page",
            command=lambda: managePage(page, root, "s")).pack()
        decipher(page)
    else:                           # Button will now navigates to Scrambler Page
        page.destroy()
        page = Frame(root)
        page.pack()
        Button(
            page,
            text="Decipher Page",
            command=lambda: managePage(page, root, "d")).pack()
        scrambler(page)

def menu():
    pass


def decipher(page):
    decipherPage = Frame(page)  # Frame for scrambler page

# --------------------------------------***Components***----------------------------------------------------------------
    intro = intro_for_decipher(decipherPage)   # title + intro (scrambler)
    question = choose_a_question(decipherPage)
    textBox, submit, undo, redo = submit_text(decipherPage, "DECIPHER!")
    codeBox = enter_code(decipherPage)

# ---------------------------------------***Display***------------------------------------------------------------------
    intro.pack()
    question.pack()
    textBox.pack()
    codeBox.pack(side=LEFT)
    submit.pack()
    undo.pack(side=LEFT)
    redo.pack(side=LEFT)


# ----------------------------------------------------------------------------------------------------------------------

    return decipherPage.pack()


def scrambler(page):
    scramblerPage = Frame(page)  # Frame for scrambler page

# --------------------------------------***Components***----------------------------------------------------------------
    intro = intro_for_scrambler(scramblerPage)  # title + intro (scrambler)
    question = choose_a_question(scramblerPage)
    textBox, submit, undo, redo = submit_text(scramblerPage, "SCRAMBLE!")
    settings = options(scramblerPage)

# ---------------------------------------***Display***------------------------------------------------------------------
    intro.pack()
    question.pack()
    textBox.pack()
    submit.pack()
    undo.pack(side=LEFT)
    redo.pack(side=LEFT)
    settings.pack(side=RIGHT)

# ----------------------------------------------------------------------------------------------------------------------
    return scramblerPage.pack()


main()
