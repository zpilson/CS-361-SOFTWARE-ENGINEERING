from tkinter import *
from resultsPage import show_results


def submit_text(page, submitButtonName):
    textBox = Text(page, undo=True)
    textBox.insert(INSERT, "Enter text here...")

    readyButton = Button(page, text=submitButtonName, command=lambda: are_you_sure(submitButtonName, textBox))

    undoButton = Button(page, text="undo", command=textBox.edit_undo)
    redoButton = Button(page, text="redo", command=textBox.edit_redo)

    return textBox, readyButton, undoButton, redoButton


def are_you_sure(submitButtonName, textBox):
    newWindow = Tk()

    Label(newWindow, text="Are you sure?").pack()
    Button(newWindow, text="Go back", command=lambda: newWindow.destroy()).pack()
    Button(newWindow, text=submitButtonName, command=lambda: i_am_sure(newWindow, textBox)).pack()

    newWindow.mainloop()


def i_am_sure(newWindow, textBox):
    newWindow.destroy()
    storeText(textBox.get("1.0", "end-1c"))


def storeText(userInput):
    print(userInput)
    with open('userInputOriginal.txt', 'w') as f:
        f.write(userInput)
    with open('userInputEdited.txt', 'w') as f:
        f.write(userInput)
    processing()


def processing():
    show_results()
