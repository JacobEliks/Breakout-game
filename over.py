from turtle import Turtle

FONT = ("Courier", 24, "normal")


class OverMessage(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')

    def write_message(self, score, length):
        self.goto(0, -160)
        if length > 0:
            self.write(f"Game Over. Your score is {score}!", align='center', font=FONT)
        else:
            self.write(f"Congrats! You won!", align='center', font=FONT)
        self.goto(0, -200)
        self.write("Press spacebar to restart",align='center', font=FONT)

    def clear_message(self):
        self.clear()
