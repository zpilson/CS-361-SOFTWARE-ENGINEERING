from tkinter import *

def main():
    # The root of everything
    root = Tk()

    farm(root)

    root.mainloop()

def farm(root):
    frame = Frame(root)
    beue(root).pack()
    return frame

def beue(root):
    return Text(root, undo=True)

def undod(root, textBox):
    return Button(root, text="undo", command=textBox.edit_undo)

main()