from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_Score()

    def update_Score(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align="center", font=("courier", 40, "bold"))
        self.goto(100, 240)
        self.write(self.r_score, align="center", font=("courier", 40, "bold"))

    def l_point(self):
        self.l_score+=1
        self.update_Score()


    def r_point(self):
        self.r_score+=1
        self.update_Score()