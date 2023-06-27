from turtle import Turtle

FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(-350, 250)
        self.score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align='left', font=FONT, )

    def increase_score(self):
        self.score += 10
        self.update_score()




