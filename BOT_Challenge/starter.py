import math
import random
from ball_class import *
from tkinter import *
import Canon
import Canon_generator as cg
root1 = Canon.root
Canon.canv = Canvas(root1, width=root1.winfo_screenwidth(), height=root1.winfo_screenheight(), bg='white')
canvas = Canon.canv
canvas.pack(fill=BOTH, expand=1)
cannon = Canon.Cannon(canvas, 30, 600)
Canon.cannon = cannon
canvas.bind('<Motion>', Canon.mouse_move_handler)
canvas.bind("<ButtonPress-1>", Canon.time_start)
canvas.bind("<ButtonRelease-1>", Canon.time_stop)
Canon.tick()
Canon.line_drawer()
root1.mainloop()
