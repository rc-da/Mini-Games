from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score_bord()
        
    def score_bord(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align='center', font=('Courier', 80))
        self.goto(100,200)
        self.write(self.r_score, align='center', font=('Courier', 80))
        

    def l_scores(self):
        self.l_score +=1
        self.score_bord()

    def r_scores(self):
        self.r_score +=1
        self.score_bord()