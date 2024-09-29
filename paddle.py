from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.teleport(x, y)
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
    def go_up(self):
        y1 = self.ycor()
        if y1 < 240:
            self.sety(y1 + 30)
    def go_down(self):
        y1 = self.ycor()
        if y1 > -240:
            self.sety(y1 - 30)