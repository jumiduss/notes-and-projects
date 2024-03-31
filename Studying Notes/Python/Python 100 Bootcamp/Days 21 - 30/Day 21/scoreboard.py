from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",8,"bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,278)
        self.update_scoreboard()
        self.hideturtle()
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        score_string = "Score: {}".format(self.score)
        self.write(score_string, move=False, align=ALIGNMENT,font=FONT)
        
    def game_over(self):
        self.write("Game Over\nFinal Score: {}".format(self.score), move=False, align=ALIGNMENT,font=FONT)