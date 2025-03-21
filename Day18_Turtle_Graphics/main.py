from turtle import Turtle, Screen

# Creating a turtle object
gogu_the_turtle = Turtle()
gogu_the_turtle.shape("turtle")
gogu_the_turtle.color("red")

# Drawing a square
gogu_the_turtle.forward(100)
gogu_the_turtle.left(90)
gogu_the_turtle.forward(100)
gogu_the_turtle.left(90)
gogu_the_turtle.forward(100)
gogu_the_turtle.left(90)
gogu_the_turtle.forward(100)
gogu_the_turtle.left(90)

screen  = Screen()
screen.exitonclick()