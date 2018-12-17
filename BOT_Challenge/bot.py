import Canon
from tkinter import *
import Canon_generator as cg
root = Canon.root
canvas = Canon.canv
canvas.pack(fill=BOTH, expand=1)
bot = cg.create(canvas, 800, 1300)
Canon.bot = bot
bot.aim(700, 200)
bot.start_time = 0
bot.stop_time = 100


def bot_fire():
    bot.fire()
    root.after(1000, bot_fire)








