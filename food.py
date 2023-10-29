from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        # Shape,penup, shapesize is actually methods of Turtle class
        # we can use them directly just because we already inherited them from our superclass.
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # we can not use entire screen we will use screen as 280x280
        random_x = random.randint(-280, 280)  # our screen is 600x600,so we are coming from -300 to +300 on both axis
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)