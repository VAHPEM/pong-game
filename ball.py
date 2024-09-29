from turtle import Turtle
import random
import paddle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(random.randint(0, 360))
        while self.heading() in (0, 90, 180, 360):
            self.setheading(random.randint(0, 361))
        self.shapesize(0.7, 0.7)
    def go_forward(self):
        self.forward(20)
    def collision(self):
        head = self.heading()
        if self.ycor() >= 280 or self.ycor() <= -280:
            if head <= 90:
                self.setheading(head + 180 + (180 - head * 2))
            elif head <= 180:
                self.setheading(head + 2 * (180 - head))
            elif head <= 270:
                self.setheading(head - 2 * (90 - (270 - head)))
            elif head <= 360:
                self.setheading(head + 2 * (360 - head))
    def exaggerate(self):
        self.clear()