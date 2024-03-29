from turtle import Turtle,Screen
 
tim = Turtle() 
screen = Screen()
 
 
def move_forwards():
    tim.forward(10)

def move_left():
    tim.left(15)
    tim.forward(10)

def move_right():
    tim.right(15)
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="r", fun=clear_screen)
screen.exitonclick()

