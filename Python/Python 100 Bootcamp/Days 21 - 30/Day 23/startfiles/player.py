from turtle import Turtle

STARTING_POSITION = (0, -262)
MOVE_DISTANCE = 25
HEADING = 90
PSCALE = 0.5

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.pencolor("black")
        self.color("lightgreen")
        self.setposition(STARTING_POSITION)
        self.shapesize(PSCALE,PSCALE)
        self.setheading(HEADING)
        
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def reset_player(self):
        self.setposition(STARTING_POSITION)