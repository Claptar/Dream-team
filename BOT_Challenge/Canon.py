import math
from tkinter import *
import graphics as gr
from PIL import Image, ImageTk
import Landskape


class Vector:
    """
    Вспомогательный класс, для векторных оперций
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def normal_vector(self):
        """
        Нахождение вектора нормального данному
        :return: вектор нормальный данному
        """
        return Vector(-self.y, self.x)

    def multiplication(self, constant):
        """
        :param constant: Константа, на которую умножается вектор
        :return:
        """
        self.x *= constant
        self.y *= constant

    def vector_scal_multiplication(self, vector):
        """
        :param vector: векор, на который умножается исходный вектор
        :return: результат скалярного умножения векторов
        """
        return self.x*vector.x + self.y*vector.y

    def sum(self, vector):
        """
        :param vector: вектор, который складываетяс с данным
        :return: результат сложения векторов
        """
        return Vector(self.x + vector.x, self.y + vector.y)

    def unit_vector(self):
        """
        :return: единичный вектор от данного
        """
        return Vector(self.x / math.sqrt(self.x ** 2 + self.y ** 2),
                      self.y / math.sqrt(self.x ** 2 + self.y ** 2))


class Cannon:
    max_velocity = 120

    def __init__(self, canvas, x, y):
        """
        :param canvas: канва, на которой происходит рисование пушки
        :param x: х координата центра пушки
        :param y: y координата центра пушки
        """
        self.canvas = canvas
        self.x = x
        self.y = y
        self.shell_num = 1
        self.direction = math.pi/4
        self.power_speed = 0
        self.cannon_diametr = 80
        self.line_length = 80
        self.line = canv.create_line(x, y,
                                     x + 110,
                                     y + 110,
                                     width=20, fill="red")
        self.oval = canv.create_oval(x - self.cannon_diametr/2,
                                     y - self.cannon_diametr/2,
                                     x + self.cannon_diametr/2,
                                     y + self.cannon_diametr/2,
                                     outline="#4B0082", fill="#4B0082")
        self.shots = 0
        self.score = 0
        self.health = 200
        self.shells = []
        self.stop_time = 0
        self.start_time = 0
        self.damage = 20
        self.fire_ready = True
        self.last_shell_x = 1000
        self.last_shell_y = 600

    def aim(self, x, y):
        """
        Меняет направление direction так, чтобы он из точки
         (self.x, self.y) указывал в точку (x, y).
        :param x: координата x, в которую целимся
        :param y: координата y, в которую целимся
        :return: None
        """
        if x > self.x:
            self.direction = math.atan((self.y - y)/(self.x - x))
            self.draw(self.x, self.y)
        else:
            self.direction = math.atan((self.y - y)/(self.x - x)) + math.pi
            self.draw(self.x, self.y)

    def fire(self):
        """
        Создаёт объект снаряда (если ещё не потрачены все снаряды)
        летящий в направлении угла direction
        со скоростью, зависящей от длительности клика мышки
        :return: экземпляр снаряда типа Shell
        """
        if len(self.shells) < 1000:
            time_length = self.stop_time - self.start_time
            if time_length < self.max_velocity:
                self.power_speed = time_length
            else:
                self.power_speed = self.max_velocity
            shell = Shell(self.x + self.line_length*math.cos(self.direction),
                          self.y + self.line_length*math.sin(self.direction),
                          self.power_speed*math.cos(self.direction), self.power_speed*math.sin(self.direction),
                          self.canvas, self.direction)
            shell.power_speed = self.power_speed
            shell.direction = self.direction
            if len(self.shells) > 1 and self.shells[len(self.shells) - 1] != 0:
                shell.previous_power = self.shells[len(self.shells) - 1].power_speed
                shell.previous_direction = self.shells[len(self.shells) - 1].direction
            self.shells.append(shell)
            self.shots += 1

        else:
            canv.create_text(200, 20, text="Закончились снаряды", font='Arial 25', )

    def draw(self, x_gun, y_gun):
        """
        Рисует дуло пушки, которое движется в зависимости от перемещений мышки
        :return:
        """
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


class Shell:
    """
    Класс шариков-снарядов
    """
    global Standard_Radius

    def __init__(self, x, y, vx, vy, canvas, direction):
        """
        :param x: x - координата снаряда
        :param y: y - координата снаряда
        :param vx: x-компонента скорости
        :param vy: y-компонента скорости
        :param canvas: канва на которой отрисовываются снаряды
        :param direction: направление выстрела снаряда
        """
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.direction = direction
        self.power_speed = 0
        self.collision = False
        self.previous_direction = 0
        self.previous_power = 0
        self.r = Standard_Radius
        x1 = x - Standard_Radius
        y1 = y - Standard_Radius
        x2 = x + Standard_Radius
        y2 = y + Standard_Radius
        self.delta_x = 0
        self.delta_y = 0

        self.canvas = canvas

        self.oval = self.canvas.create_oval(x1, y1, x2, y2, fill='red', outline="pink")
        self.x_down = 0
        self.y_down = 0

    def go(self):
        """
        Сдвигает снаряд исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        #:param dt: время элементарного перемещения
        :return: none
        """
        ax, ay = 0, G
        dt = 0.1
        self.delta_x = self.vx * dt + ax * (dt ** 2) / 2
        self.delta_y = self.vy * dt + ay * (dt ** 2) / 2
        self.x += self.delta_x
        self.y += self.delta_y
        self.vx += ax * dt
        self.vy += ay * dt
        if self.x < 1300 and (self.y > 0 and self.x > 0):
            if not Landskape.color_checker(int(self.x//1), int(self.y//1)):
                self.draw()
            else:
                if not self.collision:
                    self.collision = True
                    return [self.x, self.y]
        else:
            self.draw()

    def draw(self):
        """
        Рисует движущийся снаряд
        :return:
        """
        self.canvas.move(self.oval, self.delta_x, self.delta_y)


def mouse_move_handler(event):
    """
    Направляет дуло пушки в сторону курсора. Связывает положение курсора и направление дула.
    :param event: перемещение курсора по экрану.
    :return: Координаты курсорв мыши
    """
    cannon.aim(event.x, event.y)


def tick():
    """
        Считает время нажатия клавиши мыши,
        Заставляет двигаьтся снаряды и мишени и проверяет их на столкновение
        :return:
        """
    global time_counter
    time_counter += 1
    for g in range(len(cannon.shells)):
        if cannon.shells[g] != 0:
            cannon.shells[g].go()
            if cannon.shells[g].x < 1300 and (cannon.shells[g].y > 0 and cannon.shells[g].x > 0):
                if Landskape.color_checker(int(cannon.shells[g].x),
                                           int(cannon.shells[g].y)):
                    poof_drawer(cannon.shells[g].x, cannon.shells[g].y)
                    canv.delete(cannon.shells[g].oval)
                    cannon.shells[g] = 0
                if cannon.shells[g] != 0 and (math.sqrt(
                        (cannon.shells[g].x - bot.x) ** 2 + (cannon.shells[g].y - bot.y) ** 2)
                        < bot.cannon_diametr / 2):
                    boom_drawer(cannon.shells[g].x, cannon.shells[g].y)
                    canv.delete(cannon.shells[g].oval)
                    cannon.shells[g] = 0
                    cannon.score += 1
                    if bot.health > cannon.damage:
                        bot.health -= cannon.damage
                    else:
                        bot.health = 0
    root.after(10, tick)


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


def boom_drawer(x, y):
    global boom
    boom = canv.create_image(x, y, image=boom_image)
    root.after(100, clear_boom)


def clear_boom():
    canv.delete(boom)


def poof_drawer(x, y):
    global poof
    # canv.create_oval(x - Standard_Radius, y - Standard_Radius,
    #                  x + Standard_Radius, y + Standard_Radius,
    #                  fill=gr.color_rgb(0, 162, 232),
    #                  outline=gr.color_rgb(0, 162, 232))
    poof = canv.create_image(x, y, image=poof_image)
    root.after(100, clear_poof)


def clear_poof():
    canv.delete(poof)


def line_drawer():
    """
    отрисовка шкалы силы выстрела
    :return:
    """
    global time_checker, time_counter, line_power, line_power_max
    if time_checker:
        canv.delete(line_power)
        line_power_max = canv.create_line(20, 800, 300, 800, width=20, fill="white")
        if time_counter < 120:
            line_power = canv.create_line(20, 800,
                                          time_counter/120*280 + 20,
                                          800,
                                          width=20, fill="#87CEFA")
        elif time_counter > 120:
            line_power = canv.create_line(20, 800,
                                          300,
                                          800,
                                          width=20, fill="#87CEFA")
    root.after(100, line_drawer)


root = Toplevel()
fr = Frame(root)
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen', True)
canv = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg='white')
canv.create_rectangle(0, 0, 2000, 1100, fill=gr.color_rgb(0, 162, 232))
bg_image = ImageTk.PhotoImage(Image.open('bg.png'))
bg = canv.create_image(1534/2, 876/2, image=bg_image)
land_image = ImageTk.PhotoImage(Image.open('land.png'))
land = canv.create_image(1534/2, 876/2, image=land_image)
boom_image = ImageTk.PhotoImage(Image.open('boom.png'))
boom = canv.create_image(200, 1000, image=boom_image)
poof_image = ImageTk.PhotoImage(Image.open('poof.png'))
poof = canv.create_image(200, 1000, image=poof_image)

n = 3
time_counter = 0
time_checker = False
line_power = canv.create_line(20, 800,
                              time_counter / 100 + 20,
                              800,
                              width=20, fill="#87CEFA")
G = 9.8  # Ускорение свободного падения для снаряда.
Standard_Radius = 10
cannon = Cannon(canv, 1, 1000)
bot = Cannon(canv, 1, 10000)

