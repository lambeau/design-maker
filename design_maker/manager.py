import turtle


class Manager(object):

    __instance = None

    def __new__(cls):
        if Manager.__instance is None:
            Manager.__instance = super(Manager, cls).__new__(cls)
            turtle.setup(width=1024, height=1024, startx=16, starty=16)
            Manager.__instance.screen = turtle.Screen()
            Manager.__instance.screen.delay(0)
            Manager.__instance.pen = turtle.Turtle()
            Manager.__instance.pen.speed(0)
            Manager.__instance.pen.hideturtle()
        return Manager.__instance

    def __init__(self):
        pass
