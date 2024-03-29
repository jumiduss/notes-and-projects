from turtle import Turtle,Screen
import random


screen = Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput(title="Make your bet.",prompt="Which turtle do you think will win the race? Enter a color: ")
print(user_bet)
tim = jeff = jim = tedd = walter = samson = Turtle()
colors = ["red","orange","green","blue","yellow","purple"]
all_turtles = []

goto_loc = [-230,-150]
for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(goto_loc[0],goto_loc[1])
    goto_loc[1] += 50
    all_turtles.append(new_turtle)
race_is_on = False
if user_bet:
    race_is_on = True
winner = ''
while race_is_on:
    
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        
        if turtle.xcor() >= 100:
            winner = turtle.color()[1]
            print("{} has won the race!".format(turtle.color()[1]))
            race_is_on = False

if user_bet == winner:
        print("You won!")
else:
    print("You lost!")






screen.exitonclick()
