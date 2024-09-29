from turtle import Turtle
class Scoreboard(Turtle):
    def __init(self, x, y):
        super().__init__()
        self.point = 0
        self.color("white")
        self.teleport(x, y)
        self.write(f"Score: {self.point}", False, "center", ("Arial", 16, "normal"))
    def increase(self):
        self.point += 1
        self.clear()
        self.write(f"Score: {self.point}", False, "center", ("Arial", 16, "normal"))