from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INREMENT = 5

class Cars:
    def __init__(self):
        self.cars_right = []
        self.cars_left = []
        self.car_speed = STARTING_MOVE_DISTANCE



    def create_car_right(self):
        random_chance = random.randint(1, 10)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.pu()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(25, 150)
            new_car.goto(300, random_y)
            self.cars_right.append(new_car)

    def create_car_left(self):
        random_chance = random.randint(1, 10)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.pu()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-140, -25)
            new_car.goto(-300, random_y)
            self.cars_left.append(new_car)

    def move_cars_right(self):
        for car in self.cars_right:
            car.backward(self.car_speed)

    def move_cars_left(self):
        for car in self.cars_left:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INREMENT
