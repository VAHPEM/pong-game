import turtle
class Test():
    def __init__(self):
        self.pointb = 0
        self.pointa = 0
        self.ascore = turtle.Turtle()
        self.bscore = turtle.Turtle()
        self.ascore.color("white")
        self.ascore.teleport(350, 250)
        self.ascore.hideturtle()
        self.ascore.write(f"Score: {self.pointa}", False, "center", ("Arial", 16, "normal"))
        self.bscore.color("white")
        self.bscore.teleport(-350, 250)
        self.bscore.hideturtle()
        self.bscore.write(f"Score: {self.pointb}", False, "center", ("Arial", 16, "normal"))
    def increasea(self):
        self.pointa += 1
        self.ascore.clear()
        self.ascore.write(f"Score: {self.pointa}", False, "center", ("Arial", 16, "normal"))
    def increaseb(self):
        self.pointb += 1
        self.bscore.clear()
        self.bscore.write(f"Score: {self.pointb}", False, "center", ("Arial", 16, "normal"))