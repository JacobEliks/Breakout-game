from turtle import Screen
from ball import Ball
from paddle import Paddle
from block import BlockManager
from scoreboard import ScoreBoard
from start import StartMessage
from over import OverMessage


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)
screen.listen()

ball = Ball()
ball.goto(0, -230)
paddle = Paddle(position=(0, -270))

manager = BlockManager()
manager.layout_blocks()
scoreboard = ScoreBoard()
start = StartMessage()

screen.update()
game_is_on = False
over = OverMessage()


def begin_game():
    screen.onkey(None, " ")
    start.clear_message()
    over.clear_message()
    game_is_on = True
    scoreboard.score = 0
    scoreboard.update_score()
    screen.update()
    while game_is_on:
        screen.update()
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 280:
            ball.bounce_y()

        if ball.xcor() > 380 or ball.xcor() < -390:
            ball.bounce_x()

        if paddle.xcor() > 320:
            screen.onkey(None, "d")
        else:
            screen.onkey(paddle.go_right, "d")

        if paddle.xcor() < -330:
            screen.onkey(None, "a")
        else:
            screen.onkey(paddle.go_left, "a")

        # Detect collision with paddle
        if ball.distance(paddle) < 50 and ball.ycor() < -250:
            if ball.xcor() <= paddle.xcor() and ball.x_move > 0:
                ball.bounce_x()
            elif ball.xcor() > paddle.xcor() and ball.x_move < 0:
                ball.bounce_x()
            ball.bounce_y()

        # Detect collision with block
        for block in manager.all_blocks:
            if block.ycor() - 15 <= ball.ycor() <= block.ycor() + 15:
                if block.distance(ball) < 40:
                    ball.bounce_x()
                    block.hideturtle()
                    manager.all_blocks.remove(block)
                    scoreboard.increase_score()
            elif block.distance(ball) < 30:
                ball.bounce_y()
                block.hideturtle()
                manager.all_blocks.remove(block)
                scoreboard.increase_score()

        # Detect paddle misses
        if ball.ycor() < -290 or len(manager.all_blocks)==0:
            ball.bounce_y()
            ball.reset_position()
            paddle.reset_position()
            game_is_on = False
            manager.layout_blocks()
            screen.onkey(begin_game, " ")
            over.write_message(scoreboard.score, len(manager.all_blocks))
            screen.update()


screen.onkey(begin_game, " ")


screen.exitonclick()