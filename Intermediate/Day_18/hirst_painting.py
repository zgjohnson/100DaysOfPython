import random
from turtle import Turtle, Screen
import colorgram


def get_rgb_colors():
    rgb_colors = []
    colors = colorgram.extract('hirst painting.jpg', 26)
    print(colors[0].rgb)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        if r >= 250 and g >= 250 and b >= 250:
            continue
        else:
            rgb_colors.append((r, g, b))
    return rgb_colors


def draw_hirst_dot_painting(colors):
    x = -225
    y = -225

    for dot_count in range(1, 101):
        timmy.teleport(x, y)
        timmy.dot(20, random.choice(colors))
        x += 50
        if dot_count % 10 == 0:
            y += 50
            x = -225


timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.hideturtle()

draw_hirst_dot_painting(get_rgb_colors())

screen.exitonclick()
