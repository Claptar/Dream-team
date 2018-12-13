import math
import random
from tkinter import *
import Canon
import Canon_generator as cg
from PIL import Image, ImageTk
root1 = Canon.root
root1.overrideredirect(True)
root1.overrideredirect(False)
root1.attributes('-fullscreen', True)
canvas = Canon.canv
canvas.pack(fill=BOTH, expand=1)

ball_image = ImageTk.PhotoImage(Image.open('1.png'))
#canvas.create_image(ball_image.size[0], root1.winfo_screenheight()/2, image=ball_image)
cannon = cg.create(canvas)
bot_cannon = Canon.Cannon(canvas, 500, 600)
Canon.cannon = cannon
canvas.bind('<Motion>', Canon.mouse_move_handler)
canvas.bind("<ButtonPress-1>", Canon.time_start)
canvas.bind("<ButtonRelease-1>", Canon.time_stop)
Canon.tick()
Canon.line_drawer()
root1.mainloop()