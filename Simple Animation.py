from tkinter import *
import random
import time

WIDTH = 500
HEIGHT = 400

tk = Tk()
canvas = Canvas(tk, width = WIDTH, height = HEIGHT)
tk.title("Drawing")
canvas.pack()

ball = canvas.create_oval(10,10,60,60, fill = "orange")
xspeed = 1
yspeed = 2

while True:
    canvas.move(ball, xspeed, yspeed)
    pos = canvas.coords(ball)
    if pos[3] >= HEIGHT or pos[1] <= 0:
        yspeed = -yspeed
    if pos[2] >= WIDTH or pos[0] <= 0:
        xspeed = -xspeed
    tk.update()
    time.sleep(0.01)

tk.mainloop()