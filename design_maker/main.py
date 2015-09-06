import turtle


def initialize():
    turtle.setup(width=1024, height=1024, startx=16, starty=16)
    turtle.hideturtle()
    turtle.Screen()


def circle(radius=500):
    a = turtle.Turtle()
    a.speed(0)
    a.hideturtle()
    a.penup()
    a.right(90)
    a.forward(radius)
    a.left(90)
    a.pendown()
    a.circle(radius)
    a.penup()
    a.left(90)
    a.forward(radius)
    a.right(90)


def finish():
    turtle.exitonclick()


def main():
    initialize()
    for i in range(0, 500, 1):
        circle(i)
    finish()


if __name__ == '__main__':
    main()