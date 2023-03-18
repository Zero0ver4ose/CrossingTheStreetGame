from turtle import Turtle

class Schiggy(Turtle):
    def __init__(self):
        super().__init__()
        # create turtle object
        self.shape("turtle")
        self.pu()
        self.color("green")
        self.go_to_start()
        self.left(90)

    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(0, new_y)

    def move_back(self):
        new_y = self.ycor() - 10
        self.goto(0, new_y)

    def go_to_start(self):
        self.goto(0, -170)

    def is_at_finish_line(self):
        if self.ycor() > 180:
            return True
        else:
            return False