import math
import random
from tkinter import *
import graphics as gr
from PIL import ImageTk, Image
import Landskape as Landskape
import Canon as Canon


def find_place(x_start, x_end):
    x = random.randint(x_start, x_end)
    y = 0
    while Landskape.img.get(x, y) != Landskape.check_color:
        y += 1
    return [x, y]


def create(canvas, x_start, x_end):
    coordinates = find_place(x_start, x_end)
    return Canon.Cannon(canvas, coordinates[0], coordinates[1])

