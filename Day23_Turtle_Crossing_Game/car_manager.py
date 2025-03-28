from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
CAR_SPACING = 30  # Minimum distance between car rows
MAX_CARS_ON_SCREEN = 20  # Limit to prevent excessive spawning

class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.used_positions = set()  # Track occupied y-positions

    def create_cars(self):
        random_chance  = random.randint(1,6)
        if random_chance  == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=3)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move_cars(self):
        """Move all cars left and remove off-screen cars."""
        for car in self.cars:
            car.backward(self.speed)
        
        

    def increase_speed(self):
        """Increase speed when the player progresses."""
        self.speed += MOVE_INCREMENT
        
        
    def level_up(self):
        self.speed += MOVE_INCREMENT
