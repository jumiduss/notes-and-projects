from audioop import reverse
import random
from math import floor
from car import Car
STARTING_MOVE_DISTANCE = 5
STARTING_X_LOCATIONS = [250,200,175,125,100,150,125,75,50,0,-25,-75,-100,-150,-175,-225,-250,-300]

class Lane():
    def __init__(self, car_type, lane_ycor):
        
        self.car_speed = car_type['speed'] * STARTING_MOVE_DISTANCE
        self.car_color = car_type['color']
        self.y_cor = lane_ycor
        self.lane_start_cor = (300, self.y_cor)
        self.cars_list = []
        
    def lane_start_is_clear(self):
        if (self.cars_list[-1]).xcor() < 260:
            return True
                            
    def spawn_car(self):
        if (not self.cars_list or self.lane_start_is_clear()) and len(self.cars_list) < 5:
            if random.randint(0,1) == 1:
              self.cars_list.append(Car(self.lane_start_cor, self.car_color))
        
    def car_oob_and_remove(self): # Out of Bounds then Remove
        for car in self.cars_list:
            if car.xcor() < -280:
                del car
                    
    def move(self):
        for car in self.cars_list:
            car.forward(self.car_speed)
            
        if len(self.cars_list) > 0:
            self.car_oob_and_remove()

    def set_type(self,car_type):
        self.car_color = car_type['color']
        self.car_speed = (car_type['speed']) * 5

    def populate_lane(self):
        car_quantity = random.randrange(0,floor(len(STARTING_X_LOCATIONS) / 3))
        
        if car_quantity != 0:
            choices = random.sample(STARTING_X_LOCATIONS, k=car_quantity)
            choices.sort()        
            for i in choices:
                self.cars_list.append(Car((i,self.y_cor),self.car_color))
                
    def reset(self):
        for car in self.cars_list:
            car.setposition(500,500)