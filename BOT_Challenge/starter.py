import math
import random
from tkinter import *
import Canon
import Canon_generator as cg
root1 = Canon.root
root1.overrideredirect(True)
root1.overrideredirect(False)
root1.attributes('-fullscreen', True)
Canon.canv = Canvas(root1, width=root1.winfo_screenwidth(), height=root1.winfo_screenheight(), bg='white')
canvas = Canon.canv
canvas.pack(fill=BOTH, expand=1)
cannon = cg.create(canvas)
Canon.cannon = cannon
canvas.bind('<Motion>', Canon.mouse_move_handler)
canvas.bind("<ButtonPress-1>", Canon.time_start)
canvas.bind("<ButtonRelease-1>", Canon.time_stop)
Canon.tick()
Canon.line_drawer()
root1.mainloop()
