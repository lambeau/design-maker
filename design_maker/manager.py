import turtle


class Manager(object):

    __instance = None

    def __new__(cls):
        if Manager.__instance is None:
            Manager.__instance = super(Manager, cls).__new__(cls)
        return Manager.__instance

    def __init__(self):
        turtle.setup(width=1024, height=1024, startx=16, starty=16)
        self.screen = turtle.Screen()
        self.screen.delay(0)
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()
        
