import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

DISPLAY_TURTLES = {"water":{"color":"blue","y_cor":225},"grass":{"color":"green","y_cor":-250}}
FINISH_LINE_Y = 213

def make_area(color,position):
    new_area = Turtle()
    new_area.shape("square")
    new_area.penup()
    new_area.setheading(90)
    new_area.color(color)
    new_area.shapesize(30,5)
    new_area.setposition(0,position)

def draw_lines():
    lane_draw = Turtle()
    lane_draw.pencolor("black")
    lane_draw.pensize(5)
    lane_draw.setheading(0)
    for i in range(-200,176,25):
        lane_draw.penup()
        lane_draw.setposition(-300,i)
        lane_draw.pendown()
        lane_draw.forward(600)
    lane_draw.hideturtle()

screen = Screen()
screen.setup(600,600)
screen.title("Frogger")
screen.tracer(0)
screen.bgcolor("white")

grass = make_area(DISPLAY_TURTLES["grass"]["color"],DISPLAY_TURTLES["grass"]["y_cor"])
water = make_area(DISPLAY_TURTLES["water"]["color"],DISPLAY_TURTLES["water"]["y_cor"])
draw_lines()

car_manager = CarManager()
car_manager.populate_lanes()
scoreboard = Scoreboard()
frog = Player()

screen.listen()
screen.onkeypress(frog.move,"Up")


cycle_count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_lanes()
    
    cycle_count += 1
    if cycle_count > 5:
        car_manager.spawn_cars()
        cycle_count = 0
    
    if frog.ycor() > 175:
        # Round Survived
        screen.update()
        scoreboard.increase_score()
        car_manager.next_level()
        frog.reset_player()
        car_manager.populate_lanes()
    
    elif frog.ycor() <175 and frog.ycor() > -200:
        p_lane = car_manager.lane_ycors.index(
            (frog.position())[1])

        lane_obj = car_manager.lane_obj_list[p_lane]
        
        for car in lane_obj.cars_list:
            
            if car.distance(frog) < 10:
                frog.color("red")
                screen.update()
                time.sleep(0.1)
                frog.color("white")
                screen.update()
                time.sleep(0.1)
                frog.color("black")
                screen.update()
                time.sleep(0.1)
                scoreboard.game_over()
                game_is_on = False

    

screen.exitonclick()