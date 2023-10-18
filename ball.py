from turtle import Turtle

PACE = 10  # Speed at which ball moves


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.pace_x = PACE
        self.pace_y = PACE

    def move(self):
        pos_x = self.xcor() + self.pace_x
        pos_y = self.ycor() + self.pace_y
        self.goto(pos_x, pos_y)

    def bounce(self):
        self.pace_x *= -1  # Go away from paddle i.e x-axis
        self.move()

    def walls(self):
        self.pace_y *= -1  # Go away from wall i.e. y-axis
        self.move()

    def outbound(self):
        self.goto(0, 0)
        self.pace_x *= -1  # Change the x-axis direction from previous move. If by the time hit went out of bound on
                           # +ve x-axis, after resetting to centre it goes to -ve x-axis


