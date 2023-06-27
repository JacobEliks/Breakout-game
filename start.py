from turtle import Turtle
FONT = ("Courier", 24, "normal")

class StartMessage(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, -200)
        self.write_message()

    def write_message(self):
        self.write("Press spacebar to start", align='center', font=FONT)

    def clear_message(self):
        self.clear()
