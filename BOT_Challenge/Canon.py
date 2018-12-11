import math
import random
from tkinter import *
import graphics as gr


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
    max_velocity = 100

    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.shell_num = 1
        self.direction = math.pi/4
        self.power_speed = 0
        self.cannon_diametr = 80
        self.line_length = 80
        self.line = canv.create_line(x + 30, y + 30,
                                     x + 110,
                                     y + 110,
                                     width=20, fill="red")
        self.oval = canv.create_oval(x, y,
                                     x + self.cannon_diametr,
                                     y + self.cannon_diametr,
                                     outline="black", fill="black")

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
        if len(shells) < 10:
            time_length = self.stop_time - self.start_time
            self.power_speed = time_length
            shell = Shell(self.x + 40 + self.line_length*math.cos(self.direction),
                          self.y + 40 + self.line_length*math.sin(self.direction),
                          self.power_speed, self.power_speed, self.canvas, self.direction)

            shells.append(shell)
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


class Shell:
    global Standard_Radius

    def __init__(self, x, y, vx, vy, canvas, direction):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.direction = direction
        self.r = Standard_Radius
        x1 = x - Standard_Radius
        y1 = y - Standard_Radius
        x2 = x + Standard_Radius
        y2 = y + Standard_Radius
        self.delta_x = 0
        self.delta_y = 0

        self.canvas = canvas

        self.oval = self.canvas.create_oval(x1, y1, x2, y2, fill='red', outline="pink")

    def go(self, dt):
        """
        Сдвигает снаряд исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt: время элементарного перемещения
        :return: Движущийся снаряд
        """

        ax, ay = 0, G
        self.delta_x = self.vx * dt * math.cos(self.direction) + ax * (dt ** 2) / 2
        self.delta_y = self.vy * dt * math.sin(self.direction) + ay * (dt ** 2) / 2
        self.x += self.delta_x
        self.y += self.delta_y
        self.vx += ax * dt
        self.vy += -ay * dt

        self.draw()

        if self.y > 1000:
            self.canvas.delete(self.oval)
        if self.x > 1000:
            self.vx = -self.vx

    def draw(self):
        """
        Рисует движущийся снаряд
        :return:
        """
        self.canvas.move(self.oval, self.delta_x, self.delta_y)

    def detect_collision(self, other):
        """
        Проверяет факт соприкосновения снаряда и объекта other
        :param other: объект, который должен иметь поля x, y, r
        :return: логическое значение типа bool
        """

        length = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return length <= self.r + other.r


def hit_checker(shell, target):
    """
        :param shell: снаряд
        :param target: шарик-мишень
        :return: столкнулись или нет
        """
    if shell == 0 or target == 0:
        return False
    if (shell.x - target.x) ** 2 + (shell.y - target.y) ** 2 <= (target.r + shell.r) ** 2:
        return True


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
    global Balls, score, score_text
    global time_counter
    time_counter += 1
    for g in range(len(shells)):
        if shells[g] != 0:
            shells[g].go(0.1)
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


def line_drawer():
    global time_checker, time_counter, line_power
    if time_checker:
        canv.delete(line_power)
        line_power = canv.create_line(20, 700,
                                      time_counter + 20,
                                      700,
                                      width=20, fill="blue")
    root.after(100, line_drawer)

root = Tk()
fr = Frame(root)
root.geometry('1000x800')
canv = Canvas(root, bg='white')
im = PhotoImage()
n = 3
time_counter = 0
time_checker = False
line_power = canv.create_line(20, 700,
                              time_counter / 100 + 20,
                              700,
                              width=20, fill="blue")
G = 9.8  # Ускорение свободного падения для снаряда.
Standard_Radius = 10
Balls = []
for b in range(n):
    Balls.append(0)
score = 0
#score_text = canv.create_text(200, 60, text='Попадания score = {} '.format(score), font='Arial 25', )
shells = []
cannon = 0


