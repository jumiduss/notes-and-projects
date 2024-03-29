from turtle import Turtle

class Car(Turtle):
    def __init__(self, xycor, color):
        super().__init__()
        self.penup()
        self.shape("square")
        self.setheading(180)
        # self.shapesize(1,2)
        self.setposition(xycor)
        self.color(color)
    
    def not_visible(self):
        self.hideturtle()