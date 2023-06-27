from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class BlockManager:
    def __init__(self):
        self.all_blocks = []

    def create_block(self, position):
        new_block = Turtle("square")
        new_block.shapesize(stretch_wid=1, stretch_len=3)
        new_block.penup()
        new_block.color(random.choice(COLORS))
        new_block.goto(position)
        self.all_blocks.append(new_block)

    def layout_blocks(self):
        for block in self.all_blocks:
            block.hideturtle()
        self.all_blocks.clear()
        self.create_block(position=(-355, 200))
        for block in self.all_blocks:
            if block.xcor() >= 340 and block.ycor() <= 0:
                break
            elif block.xcor() >= 340:
                self.create_block(position=(-355, block.ycor()-30))
            else:
                self.create_block(position=(block.xcor()+70, block.ycor()))







