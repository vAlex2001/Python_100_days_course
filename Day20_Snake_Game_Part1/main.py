import turtle
import Snake
import time

# Create the screen
screen = turtle.Screen()
screen.tracer(0)
# Custom size
screen.setup(width = 600, height = 600)

# Black background
screen.bgcolor("black")

# Set the title
screen.title("Snake")

screen.listen()

snake = Snake.Snake()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


# Exit game when click the window
screen.exitonclick()