from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(600,800)
screen.title("PONG")
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

p1_score = Score(200)
p2_score = Score(-200)

ball = Ball()

running = True
while running:
    screen.update()
    time.sleep(0.05)
    
    if ball.distance(right_paddle) < 53 and ball.xcor() > 320:    
        ball.bounce('x')
    
    if ball.distance(left_paddle) < 53 and ball.xcor() < -320:
        ball.bounce('x')
    
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce('y')
        
    if ball.xcor() > 340 or ball.xcor() < -340:
        if ball.xcor() > 340:
            p1_score.increase_score()
        else:
            p2_score.increase_score()
        ball.center()

    if p1_score.score > 2:
        win1 = "Winner!"
        win2 = "Loser!!"
        break
    elif p2_score.score > 2:
        win1 = "Loser!!"
        win2 = "Winner!"
        break
    
    ball.move()

p1_score.win_loss("{}".format(win1))
p2_score.win_loss("{}".format(win2))
ball.game_over()

screen.update()










screen.exitonclick()