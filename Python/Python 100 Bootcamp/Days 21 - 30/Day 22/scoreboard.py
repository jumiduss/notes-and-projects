from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",80,"bold")

class Score(Turtle):
    def __init__(self,side):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(side,200)
        self.update_scoreboard()
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        score_string = "{}".format(self.score)
        self.write(score_string, move=False, align=ALIGNMENT,font=FONT)
        
    def win_loss(self,win_lose):
        self.clear()
        self.write("{}".format(win_lose), move=False, align=ALIGNMENT,font=FONT)