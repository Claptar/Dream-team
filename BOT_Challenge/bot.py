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
angle = 0.5


def bot_aim():
    global angle
    cannon_was_found = False
    #v_shell = 70
    num = 0
    for g in range(len(bot.shells)):
        if bot.shells[g] != 0:
            if bot.shells[g].x_down != 0:
                num = g
    if num != 0:
        if (bot.shells[num].x_down - Canon.cannon.x) < 100 and bot.shells[num].y_down - Canon.cannon.y < 100:
            cannon_was_found = True
        elif bot.shells[num].x_down < Canon.cannon.x:
            bot.stop_time -= 6
        elif bot.shells[num].x_down > Canon.cannon.x and bot.shells[num].y_down - Canon.cannon.y > 200:
            bot.stop_time += 4
            angle += math.radians(5)
        elif bot.shells[num].x_down > Canon.cannon.x and bot.shells[num].y_down - Canon.cannon.y < 200:
            bot.stop_time += 4


    # # tg_angle = (Canon.cannon.x - math.sqrt(Canon.cannon.x**2 -
    # #                                        4*Canon.cannon.x**2*Canon.G/(2*v_shell**2)
    # #                                        * (Canon.cannon.x**2*Canon.G/(2 * v_shell**2)
    # #                                           + (Canon.cannon.y - bot.y)))
    # #             / (Canon.cannon.x**2*Canon.G/(2*v_shell**2)))
    # v = math.sqrt(Canon.G*(bot.x - Canon.cannon.x)**2*(1 + tg_angle**2)/(2
    #               * (Canon.cannon.x*tg_angle - (Canon.cannon.y - bot.y))))
    # print("canon x =", Canon.cannon.x, "canon y =", Canon.cannon.y)
    # print("bot x =", bot.x, "bot y =", bot.y)
    # print("v  = ", v)
    # print("cos = ", math.cos(math.atan(tg_angle)))
    # print("angle = ", math.atan(tg_angle))
    # print("sin = ", math.sin(math.pi))
    # bot.stop_time = v


def bot_fire():
    bot_aim()
    bot.aim(bot.x - 100*math.cos(angle), bot.y - 100*math.sin(angle))
    bot.fire()
    root.after(1000, bot_fire)
    print("bot_health = ", bot.health)
    print("cannon_health = ", Canon.cannon.health)


def go():
    print("v = ", bot.stop_time)
    x_down = 0
    y_down = 0
    for g in range(len(bot.shells)):
        if bot.shells[g] != 0:
            bot.shells[g].go()
            if bot.shells[g].x < 1300 and (bot.shells[g].y > 0 and bot.shells[g].x > 0):
                if Landskape.color_checker(int(bot.shells[g].x),
                                           int(bot.shells[g].y)):
                    Canon.poof_drawer(bot.shells[g].x, bot.shells[g].y)
                    bot.shells[g + 1].x_down = bot.shells[g].x
                    bot.shells[g + 1].y_down = bot.shells[g].y
                    canvas.delete(bot.shells[g].oval)
                    bot.shells[g] = 0
                if bot.shells[g] != 0 and (math.sqrt(
                        (bot.shells[g].x - Canon.cannon.x) ** 2 + (bot.shells[g].y - Canon.cannon.y) ** 2)
                        < bot.cannon_diametr / 2):
                    Canon.boom_drawer(bot.shells[g].x, bot.shells[g].y)
                    canvas.delete(bot.shells[g].oval)
                    bot.shells[g] = 0
                    bot.score += 1
                    if Canon.cannon.health > bot.damage:
                        Canon.cannon.health -= bot.damage
                    else:
                        Canon.cannon.health = 0
    root.after(10, go)





