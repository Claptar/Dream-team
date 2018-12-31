import math
import random
from tkinter import *
import graphics as gr
from PIL import ImageTk, Image
import Canon
#(0, 162, 232)
img = PhotoImage(file="1.png")
check_color = img.get(200, 700)


def color_checker(x, y):
    return img.get(x, y) == check_color


def print_landskape():
    y = 0
    for x in range(0, 1350, 3):
        while not color_checker(x, y):
            y += 1
        Canon.canv.create_line(x, y, x, Canon.root.winfo_screenheight(), width=2, fill='orange')
        y = 0
