import math
import random
from tkinter import *
import graphics as gr
from PIL import ImageTk, Image
import Landskape
import Canon


def find_place():
    x = random.randint(0, 100)
    y = 0
    while Landskape.img.get(x, y) != Landskape.check_color:
        y += 1
    return [x, y]


def create(canvas):
    coordinates = find_place()
    return Canon.Cannon(canvas, coordinates[0], coordinates[1])

