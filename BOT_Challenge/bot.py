import Canon
from tkinter import *
import Canon_generator as cg
import Landskape
import math
import random
root = Canon.root
canvas = Canon.canv
canvas.pack(fill=BOTH, expand=1)
bot = cg.create(canvas, 800, 1300)
Canon.bot = bot
bot.aim(700, 200)
bot.start_time = 0
bot.stop_time = 70


def bot_fire():
    bot.aim(700, random.randint(200, 400))
    bot.fire()
    root.after(1000, bot_fire)
    print("bot_health = ", bot.health)
    print("cannon_health = ", Canon.cannon.health)


def go():
    for g in range(len(bot.shells)):
        if bot.shells[g] != 0:
            bot.shells[g].go(0.1)
            if bot.shells[g].x < 1300 and (bot.shells[g].y > 0 and bot.shells[g].x > 0):
                if Landskape.color_checker(int(bot.shells[g].x),
                                           int(bot.shells[g].y)):
                    Canon.poof_drawer(bot.shells[g].x, bot.shells[g].y)
                    canvas.delete(bot.shells[g].oval)
                    bot.shells[g] = 0
                if bot.shells[g] != 0 and (math.sqrt(
                        (bot.shells[g].x - Canon.cannon.x) ** 2 + (bot.shells[g].y - Canon.cannon.y) ** 2)
                        < bot.cannon_diametr / 2):
                    Canon.boom_drawer(bot.shells[g].x, bot.shells[g].y)
                    canvas.delete(bot.shells[g].oval)
                    bot.shells[g] = 0
                    bot.score += 1
                    Canon.cannon.health -= 20
    root.after(10, go)





