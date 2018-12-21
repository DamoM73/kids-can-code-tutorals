from tkinter import *
import random
import time

WIDTH = 800
HEIGHT = 600
COLOURS = ["red", "green", "blue", "orange", "yellow", "cyan", "magenta", "dodgerblue", "turquoise", "grey", "gold", "pink"]

class Ball:
    def __init__(self, colour, size):
        self.shape = canvas.create_oval(WIDTH/2,HEIGHT/2,WIDTH/2+size,HEIGHT/2+size, fill = colour)
        self.xspeed = random.randrange(-10,10)
        self.yspeed = random.randrange(-10,10)

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


balls = []
for i in range(10000):
    balls.append(Ball(random.choice(COLOURS),random.randrange(25,50)))

while True:
    for ball in balls:
        ball.move()
    tk.update()
    time.sleep(0.01)

tk.mainloop()