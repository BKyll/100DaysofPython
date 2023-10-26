from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def go_forward():
    tim.forward(10)


def go_backward():
    tim.backward(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def clear_screen():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()


screen.listen()

screen.onkey(key="w", fun=go_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=go_backward)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
