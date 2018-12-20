import math
import random
from tkinter import *
import graphics as gr
from PIL import ImageTk, Image
import Landskape
import Canon


def find_place(x_start, x_end):
    x = random.randint(x_start, x_end)
    y = 0
    while Landskape.img.get(x, y) != Landskape.check_color:
        y += 1
        print("Я не хочу работать = ", Landskape.img.get(x, y))
    return [x, y]


def create(canvas, x_start, x_end):
    coordinates = find_place(x_start, x_end)
    print("Ну давай работай = ", Landskape.img.get(coordinates[0], coordinates[1] + 50))
    return Canon.Cannon(canvas, coordinates[0], coordinates[1])

