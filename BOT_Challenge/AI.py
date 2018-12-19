from Canon import *
from Canon_generator import *
from tkinter import *


class AI:

    ai_cannon = Cannon(canvas, x, y)

    def shooting_preparation(self):
        if check_hit.x == ai_cannon.x:
            ai_cannon.aim(x + 10, y + 10)
        elif check_hit.x - x > 50:
            ai_cannon.aim(x, y + 10)


    def attack(self):
        ai_cannon.fire.power = (ai_cannon.x - cannon.x)/2

    def check_hit(self, x, y):
        """
        Получает координаты попадания ядра
        :param x, y: координаты попадания ядра
        :return:
        """


