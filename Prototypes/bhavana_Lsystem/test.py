import Tkinter as tk
import numpy as np
from math import *
import io
from PIL import Image



baselength = 25
imgwidth = 500
imgheight = 500


def draw_stem(c, depth, x1, y1, angle):
    if (depth < 1):
        return

    # deformation/sag formula
    x2 = x1 + (baselength * depth * cos(radians(angle)))
    y2 = y1 - (baselength * depth * sin(radians(angle)))
    parts = [c.create_line(x1, y1, x2, y2, width = depth*2, fill="green")]

    branch = draw_stem(c, depth-1, x2, y2, angle-30)
    branch2 = draw_stem(c, depth-1, x2, y2, angle+30)

    return parts.append(draw_stem(c, depth-1, x2, y2, angle))


def draw_plant(master):
    c = tk.Canvas(master, width=imgwidth, height=imgheight, bg="white")
    c.pack()

    # seed
    parts = draw_stem(c, 6, imgwidth/2, imgheight, 90)  
    c.update()

    return c



def save_img(c): 
    # c.postscript(file="testing.ps")
    ps = c.postscript(colormode='color')
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    img.save('test.png')



def main():
  
    master = tk.Tk()
    c = draw_plant(master) 
    save_img(c)
    master.mainloop()


if __name__ == '__main__':
    main()  
