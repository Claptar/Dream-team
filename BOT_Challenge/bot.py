import Canon as Canon
from tkinter import *
import Canon_generator as cg
import Landskape as Landskape
import math
import random
root = Canon.root
canvas = Canon.canv
canvas.pack(fill=BOTH, expand=1)
bot = cg.create(canvas, 900, 1300)
Canon.bot = bot
bot.aim(700, 200)
bot.start_time = 0
bot.stop_time = 70
angle = 0.9
cannon_was_found = False


def bot_aim():
    global angle, cannon_was_found
    if not cannon_was_found:
        if bot.fire_ready:
            if (bot.last_shell_x - Canon.cannon.x) < 100 and bot.last_shell_y - Canon.cannon.y < 100:
                cannon_was_found = True
            elif bot.last_shell_x < Canon.cannon.x:
                bot.stop_time -= 6
            elif bot.last_shell_x > Canon.cannon.x and bot.last_shell_y - Canon.cannon.y > 200:
                bot.stop_time += 4
                angle += math.radians(5)
            elif bot.last_shell_x > Canon.cannon.x and bot.last_shell_y - Canon.cannon.y < 200:
                bot.stop_time += 4
            bot.fire_ready = False


def bot_fire():
    if bot.fire_ready:
        bot_aim()
        if cannon_was_found:
            bot.aim(bot.x - 300 * math.cos(angle + math.radians(random.randint(-10, 10))),
                    bot.y - 300 * math.sin(angle + math.radians(random.randint(-10, 10))))
        else:
            bot.aim(bot.x - 100*math.cos(angle), bot.y - 100*math.sin(angle))
        bot.fire()
    bot.fire_ready = False
    root.after(700, bot_fire)


def go():
    for g in range(len(bot.shells)):
        if bot.shells[g] != 0:
            bot.shells[g].go()
            if bot.shells[g].x < 1300 and (bot.shells[g].y > 0 and bot.shells[g].x > 0):
                if Landskape.color_checker(int(bot.shells[g].x),
                                           int(bot.shells[g].y)):
                    Canon.poof_drawer(bot.shells[g].x, bot.shells[g].y)
                    if not cannon_was_found:
                        bot.last_shell_x = bot.shells[g].x
                        bot.last_shell_y = bot.shells[g].y
                    canvas.delete(bot.shells[g].oval)
                    bot.shells[g] = 0
                    bot.fire_ready = True
                if bot.shells[g] != 0 and (math.sqrt(
                        (bot.shells[g].x - Canon.cannon.x) ** 2 + (bot.shells[g].y - Canon.cannon.y) ** 2)
                        < bot.cannon_diametr / 2):
                    Canon.boom_drawer(bot.shells[g].x, bot.shells[g].y)
                    canvas.delete(bot.shells[g].oval)
                    bot.shells[g] = 0
                    bot.score += 1
                    bot.fire_ready = True
                    if Canon.cannon.health > bot.damage:
                        Canon.cannon.health -= bot.damage
                    else:
                        Canon.cannon.health = 0
    root.after(10, go)


