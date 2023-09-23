import turtle as t
import random
# import colorgram as c


# colors = c.extract('image.jpg', 30)
# color_list = []
# for c in colors:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     rgb_color = (r, g, b)
#     color_list.append(rgb_color)

color_list = [(233, 233, 236), (233, 232, 228), (236, 230, 233), (224, 234, 229), (176, 48, 79), (42, 98, 146),
              (205, 161, 94), (223, 210, 102), (137, 90, 64), (177, 164, 38), (109, 176, 207), (212, 131, 173),
              (227, 73, 49), (201, 75, 117), (88, 105, 192), (28, 143, 89), (124, 218, 207), (120, 43, 71),
              (94, 158, 65), (227, 170, 187), (131, 184, 161), (48, 187, 202), (172, 187, 222), (232, 173, 164),
              (154, 209, 219), (100, 51, 43), (34, 64, 115), (44, 80, 79), (215, 207, 37), (52, 58, 66)]

t.colormode(255)

tim = t.Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.pu()

tim.setheading(225)
tim.forward(250)
tim.setheading(0)

for y in range(10):
    tim.sety((y * 50)-250)
    for x in range(10):
        tim.setx((x * 50)-250)
        tim.dot(20, random.choice(color_list))

screen = t.Screen()
screen.exitonclick()
