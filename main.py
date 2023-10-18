from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

LEFT_PADDLE = -370
RIGHT_PADDLE = 370
TIME_DELAY = 0.1

pongScreen = Screen()
pongScreen.setup(800, 600)
pongScreen.bgcolor("black")
pongScreen.title("Pong")
pongScreen.tracer(0)

pongScreen.listen()

# level = pongScreen.textinput("Game Level", "Choose game level : EASY, MEDIUM, HARD?").lower()
# if level == "medium":
#     TIME_DELAY = 0.05
# elif level == "hard":
#     TIME_DELAY = 0.01


l_paddle = Paddle((LEFT_PADDLE, 0))
r_paddle = Paddle((RIGHT_PADDLE, 0))

pongScreen.onkey(r_paddle.up, "Up")
pongScreen.onkey(r_paddle.down, "Down")
pongScreen.onkey(l_paddle.up, "w")
pongScreen.onkey(l_paddle.down, "s")

ball = Ball()
scores = Score()

game_on = True
while game_on:
    pongScreen.update()
    time.sleep(TIME_DELAY)
    # Right paddle hits ball
    if ball.distance(r_paddle) <= 80 and ball.xcor() >= 340: # These numbers are identified after multiple hit and trials to find the maximum contact distance with paddle
        ball.bounce()
        scores.r_score += 1
        scores.update()
    # Left paddle hits ball
    elif ball.distance(l_paddle) <= 80 and ball.xcor() <= -340:
        ball.bounce()
        scores.l_score += 1
        scores.update()
    # Ball goes out of bounds right paddle
    elif ball.xcor() >= 380:
        ball.outbound()
        scores.l_score += 1
        scores.update()
    # Ball goes out of bounds left paddle
    elif ball.xcor() <= -380:
        ball.outbound()
        scores.r_score += 1
        scores.update()
    # Ball hits north or south wall
    elif ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.walls()
    else:
        ball.move()

pongScreen.exitonclick()
