from turtle import Turtle
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self,start_position):
        super().__init__()
        self.shape("square")
        self.setheading(90)
        self.shapesize(1,5)
        self.penup()
        self.color("white")
        self.start_position = start_position
        self.setposition(self.start_position)

    def up(self):
        if self.ycor() < 300:
            self.goto(self.xcor(),(self.ycor() + 20))
    
    def down(self):
        if self.ycor() > -300:
            self.goto(self.xcor(),(self.ycor() - 20))