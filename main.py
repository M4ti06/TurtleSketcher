from turtle import Screen, Turtle
import random


my_screen = Screen()
tim = Turtle()

my_screen.listen()
my_screen.colormode(255)

colors_ready = [(0, 0, 0), (202, 167, 134), (236, 243, 249), (144, 51, 99),
                (163, 167, 40), (237, 71, 121), (238, 83, 60), (17, 140, 64), (226, 117, 162), (239, 220, 72),
                (9, 141, 178), (67, 198, 218), (22, 171, 132), (158, 59, 53), (247, 231, 1), (111, 41, 86),
                (130, 187, 162), (31, 184, 199), (237, 163, 190), (244, 168, 156), (146, 217, 191), (139, 216, 224),
                (80, 36, 74), (128, 41, 35), (6, 111, 35), (187, 191, 216)]


def pen_down():
    tim.pendown()


def pen_up():
    tim.penup()


def make_dot():
    tim.dot(size=15)


index = 0


def change_color_up():
    global index
    if index == len(colors_ready)-1:
        index = len(colors_ready)-1
    else:
        index += 1
    tim.color(colors_ready[index])


def change_color_down():
    global index
    if index == 0:
        index = 0
    else:
        index -= 1
    tim.color(colors_ready[index])


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color_tuple = (r, g, b)
    return color_tuple


def switch_random_color():
    tim.color(random_color())


brush_size = 1


def brush_size_up():
    global brush_size
    tim.width(brush_size)
    brush_size += 1


def brush_size_down():
    global brush_size
    tim.width(brush_size)
    brush_size -= 1
    if brush_size == 0:
        brush_size += 1


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def take_right():
    tim.right(10)


def take_left():
    tim.left(10)


def clear_screen():
    my_screen.resetscreen()


my_screen.onkeypress(fun=move_forward, key="w")
my_screen.onkeypress(fun=move_backward, key="s")
my_screen.onkeypress(fun=take_right, key="d")
my_screen.onkeypress(fun=take_left, key="a")
my_screen.onkeypress(fun=clear_screen, key="c")
my_screen.onkeypress(fun=brush_size_down, key="z")
my_screen.onkeypress(fun=brush_size_up, key="x")
my_screen.onkeypress(fun=switch_random_color, key="r")
my_screen.onkeypress(fun=pen_up, key="f")
my_screen.onkeypress(fun=pen_down, key="v")
my_screen.onkeypress(fun=make_dot, key="t")
my_screen.onkeypress(fun=change_color_down, key="q")
my_screen.onkeypress(fun=change_color_up, key="e")

my_screen.exitonclick()