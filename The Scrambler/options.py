from tkinter import *


def options(page):
    optionFrame = Frame(page)
    selectFrame = Frame(optionFrame)

    simpleOptions(selectFrame)

    Button(optionFrame, text="Simple", command=lambda: simpleOptions(selectFrame)).pack(side=LEFT)
    Button(optionFrame, text="Advanced", command=lambda: advancedOptions(selectFrame)).pack(side=LEFT)

    selectFrame.pack()

    return optionFrame


def simpleOptions(page):
    for widgets in page.winfo_children():
        widgets.destroy()
    var1 = StringVar()
    Checkbutton(page, text="Option 1", variable=var1, onvalue=000, offvalue=000).pack()
    var2 = StringVar()
    Checkbutton(page, text="Option 2", variable=var2, onvalue=000, offvalue=000).pack()
    var3 = StringVar()
    Checkbutton(page, text="Option 3", variable=var3, onvalue=000, offvalue=000).pack()


def advancedOptions(page):
    for widgets in page.winfo_children():
        widgets.destroy()
    var1 = StringVar()
    Checkbutton(page, text="Advanced Option 1", variable=var1, onvalue=000, offvalue=000).pack()
    var2 = StringVar()
    Checkbutton(page, text="Advanced Option 2", variable=var2, onvalue=000, offvalue=000).pack()
    var3 = StringVar()
    Checkbutton(page, text="Advanced Option 3", variable=var3, onvalue=000, offvalue=000).pack()
