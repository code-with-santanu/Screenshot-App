from screenshot import *
from setDirectory import *

import tkinter as tk
import sys

if __name__ == "__main__":

    # Storage setup
    getpath = createStoragePath()
    # create a Agent object that is gonna take screenshot
    myAgent = Agent()

    # Initilize the GUI window
    root = tk.Tk()

    root.iconbitmap("./assets/myIcon.ico")
    root.geometry("250x50")

    frame = tk.Frame(root)
    frame.pack()

    button = tk.Button(frame, text="Take Screenshot",
                       command=lambda: myAgent.screenshot(getpath))
    button.pack(side=tk.LEFT)

    close = tk.Button(frame, text="close", command=sys.exit)
    close.pack(side=tk.LEFT)

    root.mainloop()
