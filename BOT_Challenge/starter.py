import math
import random
import bot
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
cannon = cg.create(canvas, 100, 300)
bot_cannon = Canon.bot
Canon.cannon = cannon


def end(event):
    raise SystemExit


canvas.bind('<Motion>', Canon.mouse_move_handler)
canvas.bind("<ButtonPress-1>", Canon.time_start)
canvas.bind("<ButtonRelease-1>", Canon.time_stop)
canvas.bind("<ButtonRelease-3>", end)
Canon.tick()
bot.bot_fire()
bot.go()
Canon.line_drawer()
bot.bot_aim()
root1.mainloop()
