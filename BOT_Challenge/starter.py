import math
import random
import bot as bot
from tkinter import *
import Canon as Canon
import Canon_generator as cg
import status as status
import Landskape as Landskape
from PIL import Image, ImageTk


def end(event):
    raise SystemExit


def death_checker():
    if Canon.cannon.health <= 0:
        print("Пушка убита")
        finish_game()
        return True
    elif Canon.bot.health <= 0:
        print("Bot убит")
        finish_game()
        return True
    print("Проверяю")
    Canon.root.after(500, death_checker)


def game_process():
    cannon = cg.create(Canon.canv, 100, 300)
    bot_cannon = Canon.bot
    Canon.cannon = cannon
    Canon.canv.bind('<Motion>', Canon.mouse_move_handler)
    Canon.canv.bind("<ButtonPress-1>", Canon.time_start)
    Canon.canv.bind("<ButtonRelease-1>", Canon.time_stop)
    Canon.canv.bind("<ButtonRelease-3>", end)
    Canon.tick()
    bot.bot_fire()
    bot.go()
    Canon.line_drawer()
    bot.bot_aim()
    status.status()
    death_checker()


def start():
    root1 = Canon.root
    root1.overrideredirect(True)
    root1.overrideredirect(False)
    root1.attributes('-fullscreen', True)
    canvas = Canon.canv
    canvas.pack(fill=BOTH, expand=1)
    btn = Button(canvas, text="Начать игру", anchor=W, command=game_process)
    btn.configure(width=10, height=2, bg="#9370DB", fg="black", font='Impact 12', relief=FLAT)
    btn.place(x=1300, y=100)
    root1.mainloop()


def finish_game():
    root2 = Tk()
    root2.overrideredirect(True)
    root2.overrideredirect(False)
    root2.attributes('-fullscreen', True)
    canvas = Canvas(root2, width=root2.winfo_screenwidth(), height=root2.winfo_screenheight(), bg='#BA55D3')
    canvas.pack()
    # bg_r_image = ImageTk.PhotoImage(Image.open('bg.png'))
    # bg_r = canvas.create_image(1534 / 2, 876 / 2, image=bg_r_image)
    if Canon.cannon.health <= 0:
        text_loss = canvas.create_text(767, 430, text='К сожалению, Вы проиграли...\n', font='Impact 24')
        text_results = canvas.create_text(767, 500,
                                          text='Вас уничтожили за {} выстрелов\n'.format(Canon.bot.score),
                                          font='Impact 18')
        text_percent = canvas.create_text(767, 570,
                                          text='Процент попадания: {} % \n'
                                          .format(int((Canon.cannon.score / Canon.cannon.shots * 100)//1)),
                                          font='Impact 18')

    if Canon.bot.health <= 0:
        text_win = canvas.create_text(767, 430, text='Поздравляем! Вы победили!\n', font='Impact 24')
        text_results = canvas.create_text(767, 500,
                                          text='Вы уничтожили противника за {} выстрелов\n'.format(
                                              Canon.cannon.score),
                                          font='Impact 18')
        text_percent = canvas.create_text(767, 570,
                                          text='Процент попадания: {} % \n'
                                          .format(int((Canon.cannon.score / Canon.cannon.shots * 100)//1)),
                                          font='Impact 18')
    canvas.bind("<ButtonRelease-3>", end)
    root2.mainloop()


start()

