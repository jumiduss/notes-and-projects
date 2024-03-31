from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.new_location()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
    
    def new_location(self):
        
        random_x = random.randrange(-280,280,20)
        random_y = random.randrange(-280,280,20)
        
        self.goto(random_x,random_y)