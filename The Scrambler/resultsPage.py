from tkinter import *


def show_results():
    with open('userInputEdited.txt', 'r') as f:
        text1 = f.read()
    with open('userInputOriginal.txt', 'r') as f:
        text2 = f.read()

    resultsPage = Tk()
    resultsPage.title("Results")

    Label(resultsPage, text="Original").pack()
    original = Text(resultsPage)
    original.insert(INSERT, text2)
    original.pack()

    Label(resultsPage, text="New").pack()
    new = Text(resultsPage)
    new.insert(INSERT, text1)
    new.pack()

    resultsPage.mainloop()