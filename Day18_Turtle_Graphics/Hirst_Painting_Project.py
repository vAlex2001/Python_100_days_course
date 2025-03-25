import colorgram
import turtle
import random

# Extract 

rgb_colors = []

colors = colorgram.extract("Day18_Turtle_Graphics\image.jpg", 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = [r,g,b]
    rgb_colors.append(new_color)
    
    
turtle.colormode(255)    
    
# Create the turtle object
gicu = turtle.Turtle()
gicu.penup()
gicu.hideturtle()

# Create the screen object
screen = turtle.Screen() 

direction = gicu.heading()

gicu.speed(0)
gicu.goto(-10, -10)

for dot_count in range(1, 101):
    gicu.dot(20, random.choice(rgb_colors))
    gicu.forward(50)
    
    if dot_count % 10 == 0:
        gicu.setheading(90)
        gicu.forward(50)
        gicu.setheading(180)
        gicu.forward(500)
        gicu.setheading(0)
        
screen.exitonclick()