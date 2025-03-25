#from turtle import Turtle, Screen
#import random
#import turtle

# Creating a turtle object
#gogu_the_turtle = turtle.Turtle()
#gogu_the_turtle.shape("turtle")
#gogu_the_turtle.color("red")

# Drawing a square
# gogu_the_turtle.forward(100)
# gogu_the_turtle.left(90)
# gogu_the_turtle.forward(100)
# gogu_the_turtle.left(90)
# gogu_the_turtle.forward(100)
# gogu_the_turtle.left(90)
# gogu_the_turtle.forward(100)
# gogu_the_turtle.left(90)

# Draw a dashed line
# for _ in range(15):
#     gogu_the_turtle.forward(10)
#     gogu_the_turtle.penup()
#     gogu_the_turtle.forward(10)
#     gogu_the_turtle.pendown()


# Draw different shapes

# Draw something
# stop = True
# while stop:
#     nr_of_sides = int(input("How many sides in your shape : "))
#     for _ in range (nr_of_sides):
#         angle = 360 / nr_of_sides
#         gogu_the_turtle.forward(100)
#         gogu_the_turtle.right(angle)
#     choice = input("Do you want to continue (y/n): ")
#     if choice == "n":
#         stop = False

# Draw a random walk

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# gogu_the_turtle.pensize(10)

# for _ in range(200):
#     gogu_the_turtle.forward(30)
#     gogu_the_turtle.setheading(random.choice(directions))
#     gogu_the_turtle.color(random.choice(colours))

# Tuples
# my_tuple = (1,2,3) different from my_list = [1,2,3]
# Tuple is immutable and non changeable.

# gogu_the_turtle.colormode(255)
# directions = [0, 90, 180, 270]
# gogu_the_turtle.pensize(10)
# # Random color
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r, g, b)
#     return random_color
    
# directions = [0, 90, 180, 270]

# for _ in range(200):
#     gogu_the_turtle.forward(30)
#     gogu_the_turtle.setheading(random.choice(directions))
#     gogu_the_turtle.color(random_color())


# screen  = turtle.Screen()
# screen.exitonclick()

import turtle
import random

# Create the turtle
gogu_the_turtle = turtle.Turtle()

# Set color mode to allow (0-255) RGB values
turtle.colormode(255)

# Set pen size
gogu_the_turtle.pensize(10)

# Random color function
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)  # Return tuple directly

# Possible movement directions
directions = [0, 90, 180, 270]

# Move the turtle
for _ in range(200):
    gogu_the_turtle.color(random_color())  # Set a random color
    gogu_the_turtle.forward(30)  # Move forward
    gogu_the_turtle.setheading(random.choice(directions))  # Change direction randomly

# Keep the turtle window open
turtle.done()