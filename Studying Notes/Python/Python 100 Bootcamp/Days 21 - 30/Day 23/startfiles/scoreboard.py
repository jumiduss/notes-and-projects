from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0,288)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        score_string = "{}".format(self.score)
        self.write(score_string, move=False, align=ALIGNMENT,font=FONT)
            
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.clear()
        self.write("Game Over")        
        
    def win_loss(self,win_lose):
        self.clear()
        self.write(f"{win_lose}", move=False, align=ALIGNMENT,font=FONT)