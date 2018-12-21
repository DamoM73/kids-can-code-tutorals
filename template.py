from tkinter import *

# DEFINE CONSTANTS
# Screen dimentions
WIDTH = 500                                     
HEIGHT = 400

# INITIALISE TKinter
tk = Tk()                                           # create a tk object
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)     # create a canvas for the object
tk.title("Name")                                 # change the window title
canvas.pack()                                       # place the canvas in window

canvas.mainloop()                                   # continue to run the canvas