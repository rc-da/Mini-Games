from turtle import Turtle 


class Ping(Turtle):


    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.color('white')
        self.goto((pos))
            

    def up(self):
        new_x = self.xcor()
        new_y = self.ycor() + 40
        self.goto(new_x, new_y)


    def down(self):
        new_x = self.xcor() 
        new_y = self.ycor() - 40
        self.goto(new_x, new_y)

        