import turtle

gicu = turtle.Turtle()
screen = turtle.Screen()

def move_forward():
    gicu.forward(10)
    
def move_backward():
    gicu.backward(10)
    
def rotate_clockwise():
    new_heading = gicu.heading() + 10
    gicu.setheading(new_heading)
        
def rotate_counterclockwise():
    new_heading = gicu.heading() - 10
    gicu.setheading(new_heading)
    
def clear_screen():
    gicu.penup()
    gicu.clear()
    gicu.home()
    gicu.pendown()

screen.listen()
# Everytime w is pressed the turtle moves forward 10 steps
screen.onkey(key = "w", fun=move_forward)
# Everytime s is pressed the turtle moves backward 10 steps
screen.onkey(key = "s", fun=move_backward)
# Everytime a is pressed the turtle rotates to the left.
screen.onkey(key = "a", fun=rotate_counterclockwise)
# Everytime a is pressed the turtle rotates to the left.
screen.onkey(key = "d", fun=rotate_clockwise)
# Everytime c is pressed the screen is reseted.

screen.exitonclick()