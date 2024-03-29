import random
from lane import Lane

MAX_LEVEL = 21
CAR_TYPES = {
    0:{"color":"purple","speed":1}, 
    1:{"color":"blue","speed":2}, 
    2:{"color":"green","speed":3}, 
    3:{"color":"yellow","speed":4}, 
    4:{"color":"orange","speed":5}, 
    5:{"color":"red","speed":6}
}

LANE_QUANTITY = 15
LANES_START_Y_COR = -187
DIST_BETWEEN_LANES = 25 
        
class CarManager():

    
    def __init__(self):
        self.lane_ycors = [-187, -162, -137, -112, -87, 
                            -62,  -37,  -12,   13,  38,
                             63,   88,  113,  138, 163] # self.set_lane_ycors()
        self.lane_obj_list = self.create_lanes()
        self.biases = [0,0,0,0,0,0]
        self.bias_counter = [0,0,0,0,0,0]
        self.level = 0 
        
    def create_lanes(self):
        lane_set = []
        
        for i in range(0,LANE_QUANTITY):
            lane_set.append(Lane(CAR_TYPES[0], self.lane_ycors[i]))
        return lane_set
    
    def set_lane_ycors(self):
        
        lane_ycor_list = [LANES_START_Y_COR]
        
        for i in range(1,LANE_QUANTITY):
            next_ycor = (i * DIST_BETWEEN_LANES) + LANES_START_Y_COR
            lane_ycor_list.append(next_ycor)        
        return lane_ycor_list
    
    def random_type(self):
        return random.choices( list(CAR_TYPES.keys()), self.biases)[0]
            
    def increment_biases(self):            
        
        #For every type of car)
        for i in range(0, len(CAR_TYPES)):
            
            # If the car is already a selection
            if self.bias_counter[i] > 0:    
                
                # If the car bais has had max value for 2 * (n-1) rounds and not already zero
                if self.bias_counter[i] > (2 * (len(CAR_TYPES) - 1)) and self.biases[i] != 0:
                    self.biases[i] -= 1
    
                else:
                    self.bias_counter[i] += 1
                    
                    # If over the max bias
                    if self.bias_counter[i] > len(CAR_TYPES):
                        self.biases[i] = len(CAR_TYPES)
    
                    else: 
                        self.biases[i] = self.bias_counter[i]
    
            else: # Break because we introduce only one type per new round
                self.bias_counter[i] = self.biases[i] = 1
                break   
    
    def move_lanes(self):
        for lane in self.lane_obj_list:
            lane.move()
    
    def populate_lanes(self):
        for lane in self.lane_obj_list:
            lane.populate_lane()
    
    def next_level(self):
        self.increment_biases()
        
        # Initiate the row. Clear it. Then set it's new value
        for i in range(0,LANE_QUANTITY):
            
            this_lane = self.lane_obj_list[i]
            this_lane.reset() 
            this_lane.cars_list.clear()
            this_lane.set_type(CAR_TYPES[self.random_type()])
    
    def spawn_cars(self):
        for lane in self.lane_obj_list:
            lane.spawn_car()
        