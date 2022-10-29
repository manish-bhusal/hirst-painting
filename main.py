# Image Extraction from colorgram

# import colorgram
# rgb_colors = []
# colors = colorgram.extract("hirst_painting.jpg", 40)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)

import random
import turtle as turtle_module

turtle_module.colormode(255)

color_list = [(240, 249, 245), (249, 238, 245), (235, 242, 249), (237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177), (216, 134, 179), (8, 186, 216), (229, 167, 200),
              (210, 25, 148), (122, 190, 160), (7, 49, 26), (34, 136, 72), (63, 20, 7), (126, 219, 234), (190, 14, 4), (109, 87, 215), (140, 217, 202), (238, 64, 34), (71, 10, 28), (10, 98, 50), (166, 181, 232), (237, 170, 159), (253, 5, 42), (9, 87, 103), (21, 35, 249), (63, 100, 8), (253, 9, 5), (0, 246, 244), (0, 250, 254)]

#  t.penup()
#     t.forward(20)
#     t.pendown()


t = turtle_module.Turtle()
t.hideturtle()


def moving_from_beginning():
    t.penup()
    t.left(180)
    # t.left(90)
    # t.setheading(180)
    t.forward(400)
    t.right(90)
    t.forward(40)
    t.right(90)


t.speed("fastest")

t.setheading(220)
t.penup()
t.forward(190)
t.setheading(0)
# t.left(140)

for _ in range(10):
    for position in range(10):
        t.dot(20, random.choice(color_list))
        t.penup()
        t.forward(40)
        t.pendown()

    moving_from_beginning()

screen = turtle_module.Screen()
screen.exitonclick()
