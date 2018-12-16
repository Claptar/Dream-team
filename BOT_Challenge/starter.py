import math
import random
from tkinter import *
import Canon
import Canon_generator as cg
import Landskape
from PIL import Image, ImageTk
root1 = Canon.root
root1.overrideredirect(True)
root1.overrideredirect(False)
root1.attributes('-fullscreen', True)
canvas = Canon.canv
canvas.pack(fill=BOTH, expand=1)

ball_image = ImageTk.PhotoImage(Image.open('1.png'))
Landskape.print_landskape()
cannon = cg.create(canvas, 0, 500)
bot_cannon = cg.create(canvas, 800, 1300)
Canon.bot = bot_cannon
Canon.cannon = cannon
canvas.bind('<Motion>', Canon.mouse_move_handler)
canvas.bind("<ButtonPress-1>", Canon.time_start)
canvas.bind("<ButtonRelease-1>", Canon.time_stop)
Canon.tick()
Canon.line_drawer()
root1.mainloop()
