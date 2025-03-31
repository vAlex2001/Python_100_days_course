import re
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.open_score_file()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("C:\Projekte\Python\Python_100_days_course\Day24_Files_Directories_Paths\SnakeGame\my_file.txt", mode='w')
            file.write(f"Highscore : {self.high_score}")
            file.close()
        self.score = 0
        self.update_scoreboard()
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def open_score_file(self):
        file = open("C:\Projekte\Python\Python_100_days_course\Day24_Files_Directories_Paths\SnakeGame\my_file.txt",mode='r')
        contents = file.read()
        self.write(f"Score: {self.score} {contents}", align=ALIGNMENT, font=FONT)
        self.search_number_in_text(contents)
        file.close()
        
    def search_number_in_text(self, text):
        match = re.search(r'\d+', text)  # Find the first occurrence of a number
        if match:
            self.high_score = int(match.group())  # Convert it to an integer
        
