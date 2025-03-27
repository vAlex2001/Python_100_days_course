from turtle import Turtle

STARTING_POSITIONS = [(-375,0), (375,0)]

class Paddle:
    
    def __init__(self):
        self.paddles = []
        self.create_paddles()
        
    def create_paddles(self):
        for position in STARTING_POSITIONS:
            self.add_paddle(position)
        
    
    def add_paddle(self, position):
        new_paddle = Turtle("square")
        new_paddle.color("white")
        new_paddle.shapesize(stretch_len = 0.5, stretch_wid = 5)
        new_paddle.penup()
        new_paddle.goto(position)
        new_paddle.speed("fastest")
        self.paddles.append(new_paddle)
        
    def move_up(self, index):
        """Moves the paddle at the given index up."""
        paddle = self.paddles[index]
        if paddle.ycor() < 250:  
            paddle.sety(paddle.ycor() + 20)

    def move_down(self, index):
        """Moves the paddle at the given index down."""
        paddle = self.paddles[index]
        if paddle.ycor() > -250:  
            paddle.sety(paddle.ycor() - 20)
            
    
        