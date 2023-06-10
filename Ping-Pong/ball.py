from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=1 , stretch_wid=1)
        self.goto(0,0)
        self.x_move = 1
        self.y_move = 1


    def move(self):
        x = self.xcor() + self.x_move 
        y = self.ycor() + self.y_move 
        self.goto(x,y)



    def bounce(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move*= -1

    def reset_pos(self):
        self.goto(0,0)
        self.bounce_x()
