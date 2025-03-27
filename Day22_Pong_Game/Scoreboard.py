from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,275)
        self.write(f"Game started !", align="center", font=("Arial", 15, "normal"))
        
    def update_scoreboard(self, index):
        self.clear()
        if index == 1:
            self.write(f"Winner is Left !", align="center", font=("Arial", 15, "normal"))
        elif index == 0:
            self.write(f"Winner is Right !", align="center", font=("Arial", 15, "normal"))
