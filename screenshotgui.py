from screenshot import *

import tkinter as tk


#creating the frame
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text = "Take Screenshot", command=screenshot)
button.pack(side = tk.LEFT)

close = tk.Button(frame, text = "close", command=quit)
close.pack(side= tk.LEFT)

root.mainloop()