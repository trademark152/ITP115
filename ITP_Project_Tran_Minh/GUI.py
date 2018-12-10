# Graphical user interface
from tkinter import *
from Application import Application

def main():
    # WINDOW:
    # Create the root window
    root = Tk()

    # modify the window
    root.title("Restaurant Management")
    root.geometry("800x800+0+0")

    # FRAMES
    # adding a Frame to a specific window
    myApplication = Application(root)


    # KICK OFF the window's event loop (always the final thing to happen)
    root.mainloop()    # show the window

main()