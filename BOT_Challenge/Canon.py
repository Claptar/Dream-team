import math
import random
from ball_class import *
from tkinter import *
root = Tk()
fr = Frame(root)
root.geometry('1000x800')
canv = Canvas(root, bg='white')
line_power = canv.create_line(20, 700,
                              time_counter / 100 + 20,
                              700,
                              width=20, fill="blue")


class Cannon:
    max_velocity = 100

    def __init__(self, canvas):
        self.canvas = canvas
        self.x = x = -30
        self.y = y = 550
        self.shell_num = 1
        self.direction = math.pi/4
        self.power_speed = 0
        self.cannon_diametr = 80
        self.line_length = 80
        self.line = canvas.create_line(x + 30, y + 30,
                                     x + 110,
                                     y + 110,
                                     width=20, fill="red")
        self.oval = canv.create_oval(x, y,
                                     x + self.cannon_diametr,
                                     y + self.cannon_diametr,
                                     outline="black", fill="black")
        self.shells = []

    def aim(self, x, y):
        """
        Меняет направление direction так, чтобы он из точки
         (self.x, self.y) указывал в точку (x, y).
        :param x: координата x, в которую целимся
        :param y: координата y, в которую целимся
        :return: None
        """

        self.direction = math.atan((self.y - y)/(self.x - x))

        self.draw(self.x+40, self.y+40)

    def fire(self):
        """
        Создаёт объект снаряда (если ещё не потрачены все снаряды)
        летящий в направлении угла direction
        со скоростью, зависящей от длительности клика мышки
        :return: экземпляр снаряда типа Shell
        """
        if len(self.shells) < 10:
            time_length = self.stop_time - self.start_time
            self.power_speed = time_length
            shell = Ball(self.x + 40 + self.line_length*math.cos(self.direction),
                          self.y + 40 + self.line_length*math.sin(self.direction),
                          self.power_speed, self.power_speed, self.canvas, self.direction)

            self.shells.append(shell)
        else:
            canv.create_text(200, 20, text="Закончились снаряды", font='Arial 25', )
            print("Закончились снаряды")

    def draw(self, x_gun, y_gun):
        """
        Рисует дуло пушки, которое движется в зависимости от перемещений мышки
        :return:
        """
        global y_end
        self.canvas.delete(self.line)
        x_start = x_gun + math.cos(self.direction)*self.cannon_diametr/8
        y_start = y_gun + math.sin(self.direction) * self.cannon_diametr / 8
        x_end = x_gun + self.line_length*math.cos(self.direction)
        y_end = y_gun + self.line_length*math.sin(self.direction)
        self.line = self.canvas.create_line(
            x_start,
            y_start,
            x_end,
            y_end, width=20, fill="red"
        )


def time_start(event):
    """
    Включает счетчик в момент нажания левой клавиши мыши
    :param event: Момент нажатия левой клавиши
    :return: Начальное значение времени
    """
    global time_counter, time_checker
    time_counter = 0
    time_checker = True
    cannon.start_time = time_counter


def time_stop(event):
    """
    Выключает счетчик после отпускания левой клавиши
    Обнуляет счетчик
    Запускает снаряд в момент момент отпускания левой клавиши
    :param event: Момент отпускания левой клавиши
    :return: Конечное значение времени
    """
    global time_counter, time_checker, line_power
    cannon.stop_time = time_counter
    cannon.fire()
    canv.delete(line_power)
    time_checker = False


def line_drawer():
    global time_checker, time_counter, line_power
    if time_checker:
        canv.delete(line_power)
        line_power = canv.create_line(20, 700,
                                      time_counter + 20,
                                      700,
                                      width=20, fill="blue")
    root.after(100, line_drawer)


def mouse_move_handler(event):
    """
    Направляет дуло пушки в сторону курсора
    :param event: перемещение курсора по экрану
    :return: Координаты курсорв мыши
    """
    cannon.aim(event.x, event.y)


def tick():
    """
        Считает время нажатия клавиши мыши,
        Заставляет двигаьтся снаряды и мишени и проверяет их на столкновение
        :return:
        """
    global score, score_text
    global time_counter
    time_counter += 1
    for g in range(len(cannon.shells)):
        if cannon.shells[g] != 0:
            cannon.shells[g].go(0.1)
    root.after(10, tick)


canv.pack(fill=BOTH, expand=1)

canv.bind('<Motion>', mouse_move_handler)
canv.bind("<ButtonPress-1>", time_start)
canv.bind("<ButtonRelease-1>", time_stop)
cannon = Cannon(canv)
root.mainloop()
