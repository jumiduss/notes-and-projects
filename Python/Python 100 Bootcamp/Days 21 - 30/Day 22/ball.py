from turtle import Turtle

PADDLE_BOUNCE_DIR = [90,-90,-90,90]
WALL_BOUNCE_DIR = [270,90,-90,-270]

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_mov = 10
        self.y_mov = 10
        

        
        
    def center(self):
        self.setposition(0,0)

    def move(self):
        self.setposition(self.xcor() + self.x_mov,  self.ycor() + self.y_mov)
    
    def bounce(self,axis):
        if axis == 'x':
            self.x_mov *= -1
        elif axis == 'y':
            self.y_mov *= -1
    
    def game_over(self):
        self.hideturtle()
        self.shapesize(10,10)
        self.goto(0,0)
        self.clear()
        self.write("GAME OVER", move=False, align='center',font=("Arial",64,"bold"))