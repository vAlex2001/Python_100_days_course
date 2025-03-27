from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed("fastest")
        
        # Initial velocity components (dx, dy)
        self.dx = 1.5  # Horizontal speed (right direction)
        self.dy = 1.5  # Vertical speed (upward direction)

    def move(self):
        """Move the ball based on its velocity (dx, dy)."""
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce_y(self):
        """Invert the vertical direction (bounce off top/bottom walls)."""
        self.dy *= -1

    def bounce_x(self):
        """Invert the horizontal direction (bounce off left/right walls)."""
        self.dx *= -1

    def reset_position(self):
        """Reset the ball to the center with a random direction."""
        self.goto(0, 0)
        self.dx *= -1  # Invert direction after reset
    
    def ball_reset(self):
        self.goto(0,0)
        self.bounce_x()