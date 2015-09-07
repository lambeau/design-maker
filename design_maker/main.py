import turtle
import math

s = None
t = turtle.Turtle()


def initialize():
    turtle.setup(width=1024, height=1024, startx=16, starty=16)
    global s, t
    s = turtle.Screen()
    s.delay(0)
    t.speed(0)
    t.hideturtle()


def circle(radius=500):
    t.penup()
    t.right(90)
    t.forward(radius)
    t.left(90)
    t.pendown()
    t.circle(radius)
    t.penup()
    t.left(90)
    t.forward(radius)
    t.right(90)


def circle_of_circles(big_radius=300, count=12):
    angle = int(360 / count)
    start = t.position()
    heading = t.heading()
    t.penup()
    t.forward(big_radius)
    t.left(90)
    for i in range(0, 360, angle):
        t.penup()
        t.setposition(start)
        t.setheading(heading)
        t.left(i)
        t.forward(big_radius)
        t.pendown()
        circle(get_side_length(big_radius, count) / 2)


def get_side_length(circumradius, sides):
    return circumradius * 2 * math.sin(math.pi / sides)


def finish():
    s.getcanvas().postscript(file='output.eps')
    s.exitonclick()


def main():
    initialize()
    count = 9
    i = 10
    while i < 400:
        t.home()
        circle(i + i * math.sin(math.pi / count))
        circle_of_circles(big_radius=i, count=count)
        new_count = count + 1
        while 360 % new_count != 0:
            new_count += 1
        i = (i * (1 + math.sin(math.pi / count))) / (1 - math.sin(math.pi / new_count))
        count = new_count
    finish()


if __name__ == '__main__':
    main()
