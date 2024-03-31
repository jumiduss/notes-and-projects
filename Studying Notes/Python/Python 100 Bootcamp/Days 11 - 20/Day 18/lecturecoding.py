from turtle import Turtle, Screen, backward, colormode, forward, heading, left, pencolor, pendown, penup, right
import random


screen = Screen()
timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')

# Challenge 1: Draw a square
def square(distance):
    for i in range(0,4):
        left(90)
        forward(distance)
        
#square(100)

# Challenge 2: Alternate line draw every 10 px for 500 distance

def dashed_line():
    for i in range(0,500,10):
        if ((i/10)%2) == 0:
            pendown()
        else:
            penup()
            
        forward(10)
#dashed_line()

# Challenge 3: Draw polygons from number_of_edges = 3 to 10 with random color every poly
def randvar():
    return random.randrange(1,255)

def draw_poly(n_max_sides,distance):
    for j in range(3,(n_max_sides + 1)):
        turn_angle = 360 / j
        pencolor(randvar(),randvar(),randvar())
        for i in range(0,j):
            right(turn_angle)
            forward(distance)
#screen.colormode(255)
#draw_poly(10,50)

# Challenge 4: Have timmy perform a random walk with random colors
def random_color():
    return randvar(),randvar(),randvar()

def random_walk(n_times):
    for i in range(0,(n_times + 1)):
        timmy.color(random_color())
        steps = int(random.random() * 100)
        angle = int(random.randrange(0,4,1))*90
        timmy.setheading(angle)
        timmy.forward(steps)
                       
# screen.colormode(255)
# random_walk(10)

# Challenge 5: Draw a spirograph with circles
def spirograph(radii,number_of_circles):
    thead = 0
    for i in range(0, number_of_circles):
        timmy.color(random_color())
        timmy.circle(radii)
        thead += 360 / number_of_circles
        timmy.setheading(thead)
    

screen.colormode(255)
spirograph(50,18)    
    
    
    

screen.exitonclick()