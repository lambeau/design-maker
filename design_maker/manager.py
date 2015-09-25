import turtle


class Manager(object):

    _instance = None

    def __new__(cls):
        if Manager._instance is None:
            Manager._instance = super(Manager, cls).__new__(cls)
            turtle.setup(width=1024, height=1024, startx=16, starty=16)
            Manager._instance.screen = turtle.Screen()
            Manager._instance.screen.delay(0)
            Manager._instance.pen = turtle.Turtle()
            Manager._instance.pen.speed(0)
            Manager._instance.pen.hideturtle()
        return Manager._instance

    def __init__(self):
        self.state = (self.pen.position(), self.pen.heading())

    def get_state(self):
        return self.state

    def forward(self, x):
        pass

    def left(self, x):
        pass

    def reset(self):
        pass
