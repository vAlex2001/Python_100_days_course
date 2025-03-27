import turtle
import Paddle
import time
import Ball
import Scoreboard

LEFT = 0
RIGHT = 1

# Create the screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

# Create the paddle object
paddle = Paddle.Paddle()

# Create the ball object
ball = Ball.Ball()

# Create the scoreboard object
scoreboard = Scoreboard.Scoreboard()

# Dictionary to track key states (True = key held down)
key_states = {"w": False, "s": False, "Up": False, "Down": False}

# Function to move paddles while key is held
def move_paddle_while_pressed():
    if key_states["w"]:
        paddle.move_up(0)
    if key_states["s"]:
        paddle.move_down(0)
    if key_states["Up"]:
        paddle.move_up(1)
    if key_states["Down"]:
        paddle.move_down(1)
        
def update_speed(ball):
    ball.dx += 0.5  # Horizontal speed (right direction)
    ball.dy += 0.5  # Vertical speed (upward direction)
        
# Functions to start/stop movement when key is pressed/released
def key_press(key):
    key_states[key] = True

def key_release(key):
    key_states[key] = False

# Bind movement functions to keys
# Lambda creates an anonymous function that delays execution until the event (w key press) happens.
# Best Practice: Use lambda to dynamically pass arguments to functions in event listeners!

screen.onkeypress(lambda: paddle.move_up(0), "w")    # Left paddle up
screen.onkeypress(lambda: paddle.move_down(0), "s")  # Left paddle down
screen.onkeypress(lambda: paddle.move_up(1), "Up")   # Right paddle up
screen.onkeypress(lambda: paddle.move_down(1), "Down")  # Right paddle down

# Run the game loop
game_is_on = True

while game_is_on:
    ball.move()
    screen.update()
    time.sleep(0.01)
    
    # Check for collisions with walls (top and bottom)
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
        update_speed(ball)

    #Detect collision with paddle
    if ball.distance(paddle.paddles[RIGHT]) < 50 and ball.xcor() > 360 or ball.distance(paddle.paddles[LEFT]) < 50 and ball.xcor() < -360:
        ball.bounce_x()
        update_speed(ball)
        
    # Check if the ball left the screen
    if ball.xcor() > 400:
        scoreboard.update_scoreboard(RIGHT)
        ball.ball_reset()
        game_is_on = False
    elif ball.xcor() < -400:
        scoreboard.update_scoreboard(LEFT)
        ball.ball_reset()
        game_is_on = False
        
# Keep the window open
screen.exitonclick()



