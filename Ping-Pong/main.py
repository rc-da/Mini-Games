from turtle import Screen, Turtle
from ping import Ping
from ball import Ball
from score import Score

screen = Screen()
screen.bgcolor('black')
screen.title("PING PONG")
screen.setup(width = 800, height = 600)
screen.tracer(0)

r_paddle = Ping((350,0))
l_paddle = Ping((-350,0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(l_paddle.up , 'w')
screen.onkey(l_paddle.down , 's')
screen.onkey(r_paddle.up , 'Up')
screen.onkey(r_paddle.down , 'Down')

game = True

while game:
    screen.update()
    ball.move()

    if ball.ycor() > 300 or ball.ycor() < -300 :
        ball.bounce()

    if  ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle)<50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.reset_pos()
        score.r_scores()

    if ball.xcor() < -390:
        ball.reset_pos()
        score.l_scores()
    

screen.exitonclick()