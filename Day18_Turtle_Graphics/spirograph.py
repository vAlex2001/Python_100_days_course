# Draw a spirograph

import random
import turtle

# Create the turtle
gogu_the_turtle = turtle.Turtle()

# Set color mode to allow (0, 255) RGB values
turtle.colormode(255)

# Set pen size
gogu_the_turtle.pensize(2)
gogu_the_turtle.speed(0)

# Random color function
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)  # Return tuple

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        gogu_the_turtle.color(random_color())
        gogu_the_turtle.circle(100)
        gogu_the_turtle.setheading(gogu_the_turtle.heading() + size_of_gap)

# Possible movement directions
directions = [0, 90, 180, 270]

current_heading = gogu_the_turtle.heading()

# Draw a spirograph
draw_spirograph(10)
    
    

screen = turtle.Screen()
screen.exitonclick()