from tkinter import *
import random

tk = Tk()
canvas = Canvas(tk, width=500, height=400)
tk.title("Drawing")
canvas.pack()

canvas.create_line(0,0, 500, 400)
canvas.create_rectangle(100,300, 200, 400, fill = "blue")
canvas.create_oval(100, 100, 200, 200, fill="green")
canvas.create_polygon(300,300, 400,100, 500,200, fill="purple")

for i in range(100):
    x1 = random.randrange(500)
    y1 = random.randrange(400)
    x2 = random.randrange(500)
    y2 = random.randrange(400)
    canvas.create_rectangle(x1,y1,x2,y2)

canvas.mainloop()