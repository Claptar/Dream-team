from tkinter import *
from BOT_Challenge.Canon import *
import time

canv.pack(fill=BOTH, expand=1)
f_top = Frame()
f_bot = Frame()

#FIXME: Залить всю в одну функцию - сделать что-то типа main


def status():
    """
    Каждую секунду считывает уровень здоровье и
    количество оставшихся снарядов и выводит их на экран
    :return:
    """
    root.after(500, status)
    current_hero_health = cannon.health
    current_hero_shells_number = len(cannon.shells) - cannon.shots
    current_ai_health = bot.health
    current_ai_shells_number = len(bot.shells) - bot.shots
    l1 = Label(f_top, bd=5, text='Текущее здоровье: {}\n'.format(current_hero_health),
               font='Arial 20', bg='#20B2AA')
    l2 = Label(f_bot, bd=5, text='Осталось снарядов: {}'.format(current_hero_shells_number),
               font='Arial 20', bg='#20B2AA')
    l3 = Label(f_top, bd=5, text='Текущее здоровье: {}\n'.format(current_ai_health),
               font='Arial 20', bg='#CD5C5C')
    l4 = Label(f_bot, bd=5, text='Осталось снарядов: {}'.format(current_ai_shells_number),
               font='Arial 20', bg='#CD5C5C')
    f_top.pack()
    f_bot.pack()
    l1.pack(side=LEFT)
    l2.pack(side=LEFT)
    l3.pack(side=LEFT)
    l4.pack(side=LEFT)
    # text_hero = Text(width=50, height=10)
    # text_hero.pack(side=LEFT)
    # text_hero.insert(1.0, 'Текущее здоровье: {}\n'.format(current_hero_health), '\n',
    #                  'Осталось снарядов: {}'.format(current_hero_shells_number))
    # text_ai = Text(width=50, height=10)
    # text_ai.pack(side=RIGHT)
    # text_ai.insert(1.0, 'Текущее здоровье: {}\n'.format(current_ai_health), '\n',
    #                'Осталось снарядов: {}'.format(current_ai_shells_number))


def tick(timer):
    """
    Показывает, сколько времени идет бой.
    :param timer:
    :return:
    """
    canv.delete(timer)
    timer = canv.create_text(400, 50, text=time.strftime('%H:%M:%S'), font='Arial 20')
    root.after(100, tick, timer)


timer = canv.create_text(400, 300, text=time.strftime('%H:%M:%S'), font='Arial 25')
root.after_idle(tick, timer)
root.after_idle(status)

root.mainloop()
