import sys
import Tkinter as tk
import numpy as np
from math import *
import io
from PIL import Image




# imgwidth = 500
# imgheight = 500

def next_x_point(x1, length, angle):
    return int(x1 + (length * cos(radians(angle))))

def next_y_point(y1, length, angle):
    return int(y1 + (length * sin(radians(angle))))

def parse_seed(seed_str, turn_angle, baselength, basewidth = 3.0, angle=90.0):
    segments = []

    x1 = y1 = 0
    for c in seed_str.strip("\"\' "):
        if c == 'F':
            x2 = next_x_point(x1, baselength, angle)
            y2 = next_y_point(y1, baselength, angle)
            # drawline tuple
            segments += [(x1, y1, x2, y2, basewidth, baselength, angle)]
        elif c == '+':
            angle += turn_angle
        elif c == '-':
            angle -= turn_angle

    return segments



def parse_replacement_rule(replace_rule_str, turn_angle, subdepth=0):
    rule = replace_rule_str.strip("\"\' ")

    # get number of segments original is being divided into
    n_segs = 0
    nested = 0
    for c in rule:
        if c == 'F' and nested == 0: n_segs += 1
        if c == '[': nested += 1
        if c == ']': nested -= 1

    segments = []
    substr = ""
    angle = 0
    nested = 0
    for c in rule:
        # TODO: dont strip the brackets from the subnests!!!!
        if c == ']':
            if nested == 1:
                segments.append(parse_replacement_rule(substr, turn_angle, subdepth=subdepth+1))
                substr = ""
            else:
                # if inside brackets, just store the symbol
                substr += c
            nested -= 1

        elif c == '[':
            if nested > 0:
                # if inside brackets, just store the symbol
                substr += c
            nested += 1

        elif c == 'F':
            if nested > 0:
                # if inside brackets, just store the symbol
                substr += c
            else:
                # rule tuple
                segments += [((lambda x, l, a: next_x_point(x, l / n_segs, a + angle)),
                        (lambda y, l, a: next_y_point(y, l / n_segs, a + angle)),
                        # (lambda w, d: ceil(w / (d + subdepth))),
                        (lambda w, d: w),
                        (lambda l: l / n_segs),
                        (lambda a: a + angle))]
        elif c == '+':
            if nested > 0:
                # if inside brackets, just store the symbol
                substr += c
            else:
                angle += turn_angle
        elif c == '-':
            if nested > 0:
                # if inside brackets, just store the symbol
                substr += c
            else:
                angle -= turn_angle

    return segments


def generate_parts(original, replace_rule, depth, curr_depth=1):

    if curr_depth > depth:
        return original

    parts = []

    def apply_rule(x1, y1, width, length, angle, replace_rule):
        newparts = []
        new_width = width
        new_length = length
        new_angle = angle

        for rule in replace_rule:
            if isinstance(rule, list):
                newparts += apply_rule(x1, y1, new_width, new_length, new_angle, rule)
            else:            
                x2 = rule[0](x1, length, angle)
                y2 = rule[1](y1, length, angle)
                new_width = rule[2](width, curr_depth)
                new_length = rule[3](length)
                new_angle = rule[4](angle)

                # drawline tuple
                newparts += [(x1, y1, x2, y2, new_width, new_length, new_angle)]

                x1 = x2
                y1 = y2

        return newparts


    # assume all parts are F
    for s in original:
        parts += apply_rule(s[0], s[1], s[4], s[5], s[6], replace_rule)
        

    return generate_parts(parts, replace_rule, depth, curr_depth + 1)






# def draw_stem(c, depth, x1, y1, angle):
#     if (depth < 1):
#         return

#     baselength = 25

#     x2 = next_x_point(x1, baselength * depth, angle)
#     y2 = next_y_point(y1, -1.0 * baselength * depth, angle)
#     parts = [c.create_line(x1, y1, x2, y2, width = depth*2, fill="black", capstyle=tk.ROUND)]

#     branch = draw_stem(c, depth-1, x2, y2, angle-30)
#     branch2 = draw_stem(c, depth-1, x2, y2, angle+30)

#     return parts.append(draw_stem(c, depth-1, x2, y2, angle))


# def draw_plant(master):
#     c = tk.Canvas(master, width=imgwidth, height=imgheight, bg="white")
#     c.pack()

#     # seed
#     parts = draw_stem(c, 5, imgwidth/2, imgheight, 90)  
#     c.update()

#     return c


def draw_plant(master, parts):


    # calculate the needed size of canvas
    xpoints = [n[2] for n in parts]
    ypoints = [n[3] for n in parts]
    xpoints += [parts[0][0]]
    ypoints += [parts[0][1]]
    imgwidth = max(xpoints) - min(xpoints)
    imgheight = max(ypoints) - min(ypoints)

    print(parts)

    c = tk.Canvas(master, width=imgwidth, height=imgheight, bg="white")
    c.pack()

    for part in parts:
        c.create_line(part[0] - min(xpoints), max(ypoints) - part[1], part[2] - min(xpoints), max(ypoints) - part[3], width=part[4], fill="black", capstyle=tk.ROUND)
    c.update()

    return c



def save_img(c): 
    # c.postscript(file="testing.ps")
    ps = c.postscript(colormode='color')
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    img.save('test.png')


# TODO: use argparse t
# TODO: add decay rule option
# TODO: add randomizer option
def main():
    
    baselength = 300

    if len(sys.argv) > 1:
        depth = int(sys.argv[1])
        angle = float(sys.argv[2])
        seed_str = sys.argv[3]
        replace_rule_str = sys.argv[4]

        seed = parse_seed(seed_str, angle, baselength)
        replace_rule = parse_replacement_rule(replace_rule_str, angle)
        parts = generate_parts(seed, replace_rule, depth)

        master = tk.Tk()
        c = draw_plant(master, parts) 
        save_img(c)
        master.mainloop()

    else:
        print("Need command line arguments")


if __name__ == '__main__':
    main()  
