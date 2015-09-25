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

    def __enter__(self):
        self._enter_state = self.get_state()
        return self

    def __exit__(self, type, value, traceback):
        self.pen.setposition(self._enter_state[0])
        self.pen.setheading(self._enter_state[1])

    def get_state(self):
        return (self.pen.position(), self.pen.heading())

    def forward(self, x):
        self.pen.forward(x)
