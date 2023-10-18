from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pad_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(pad_pos)

    def up(self):
        px = self.xcor()
        py = self.ycor()
        if self.distance(px, 300) > 40:
            self.goto(px, py + 20)

    def down(self):
        px = self.xcor()
        py = self.ycor()
        if self.distance(px, -300) > 60:
            self.goto(px, py - 20)

