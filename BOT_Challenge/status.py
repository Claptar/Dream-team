from Canon import *
from bot import *


start_cannon_health = canv.create_rectangle(Canon.cannon.x, Canon.cannon.y + 50,
                                            Canon.cannon.x + 200,  Canon.cannon.y + 70,
                                            fill='white', outline='black')
current_cannon_health = canv.create_rectangle(Canon.cannon.x, Canon.cannon.y + 50,
                                              Canon.cannon.x + Canon.cannon.health/200*200,
                                              Canon.cannon.y + 70, fill='#00FF00', outline='black')
text_cannon_health = canv.create_text(Canon.cannon.x, Canon.cannon.y + 50,
                                      text='Здоровье {} / 200'. format(Canon.cannon.health),
                                      font='arial 12')

start_bot_health = canv.create_rectangle(bot.x, bot.y + 50, bot.x + 200,  bot.y + 70,
                                         fill='white', outline='black')
current_bot_health = canv.create_rectangle(bot.x, bot.y + 50, bot.x + bot.health/200*200, bot.y + 70,
                                           fill='#DC143C', outline='black')
text_bot_health = canv.create_text(bot.x + 100, bot.y + 60, text=' {} / 200'.format(Canon.bot.health),
                                   font='arial 12')


def status():
    """
    Каждую секунду считывает уровень здоровье и выводит его на экран
    :return:
    """
    global current_cannon_health, text_cannon_health, current_bot_health, text_bot_health
    canv.delete(current_cannon_health, text_cannon_health, current_bot_health, text_bot_health)
    start_cannon_health = canv.create_rectangle(Canon.cannon.x, Canon.cannon.y + 50,
                                                Canon.cannon.x + 200, Canon.cannon.y + 70,
                                                fill='white', outline='black')
    current_cannon_health = canv.create_rectangle(Canon.cannon.x, Canon.cannon.y + 50,
                                                  Canon.cannon.x + Canon.cannon.health/200*200,
                                                  Canon.cannon.y + 70, fill='#00FF00', outline='black')
    text_cannon_health = canv.create_text(Canon.cannon.x + 100, Canon.cannon.y + 60,
                                          text='{} / 200'.format(Canon.cannon.health),
                                          font='arial 12')
    current_bot_health = canv.create_rectangle(bot.x, bot.y + 50, bot.x + bot.health / 200 * 200, bot.y + 70,
                                               fill='#DC143C', outline='black')
    text_bot_health = canv.create_text(bot.x + 100, bot.y + 60, text=' {} / 200'.format(Canon.bot.health),
                                       font='arial 12')
    root.after(500, status)
