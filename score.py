from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-190, 250)
        self.write(self.l_score, True, font=("Arial", 15, "normal"))
        self.goto(190, 250)
        self.write(self.r_score, True, font=("Arial", 15, "normal"))