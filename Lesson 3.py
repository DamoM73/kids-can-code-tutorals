from tkinter import *
import random
import time

WIDTH = 800
HEIGHT = 600

class Ball:
    def __init__(self, colour, size):
        self.shape = canvas.create_oval(0,0,size,size, fill = colour)
        self.xspeed = random.randrange(1,8)
        self.yspeed = random.randrange(1,8)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed

tk = Tk()
canvas = Canvas(tk, width = WIDTH, height = HEIGHT)
tk.title("Drawing")
canvas.pack()

newball1 = Ball("red", 50)
newball2 = Ball("green", 100)

while True:
    newball1.move()
    newball2.move()
    tk.update()
    time.sleep(0.01)

tk.mainloop()