from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        randomx = random.randint(-280, 280)
        randomy = random.randint(-280, 280) 
        self.goto(randomx, randomy)    
    
    def refresh(self):
        randomx = random.randint(-280, 280)
        randomy = random.randint(-280, 280) 
        self.goto(randomx, randomy)