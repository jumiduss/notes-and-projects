from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake():

    def __init__(self):
        self.segments = [] 
        self.create_snake()
        self.head = self.segments[0]
        
        
    def create_snake(self):
               
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def collision(self):
        for link in self.segments[1:]:
            print("head" + str(self.head.position()))
            print("link" + str(link.position()))
            if self.head.distance(link) < 10:
                return True 
        return False
        
    def extend(self):
        self.add_segment(self.segments[-1].position())   
    
    def move(self):
        for i in range((len(self.segments)-1),0,-1):
            next_position = self.segments[i - 1].position()
            self.segments[i].setposition(next_position)
        self.segments[0].forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)