from turtle import Screen, Turtle
from schiggy import Schiggy
from levelboard import LevelBoard
from traffic import Cars
import time

screen = Screen()
screen.setup(600,400)
screen.title("Cross the Street")
screen.tracer(0)
line = Turtle(shape="square")
line.pu()
line.color("grey")
line.shapesize(0.5, 0.5)
line.goto(-300,0)
line.pd()
line.pensize(5)
line.goto(300,0)

schiggy = Schiggy()
levelboard = LevelBoard()
car = Cars()

screen.listen()
screen.onkey(schiggy.move_up, "Up")
screen.onkey(schiggy.move_back, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car_right()
    car.create_car_left()
    car.move_cars_right()
    car.move_cars_left()
    for i in car.cars_right:
        if i.distance(schiggy) < 22:
            levelboard.game_over()
            game_is_on = False

    for i in car.cars_left:
        if i.distance(schiggy) < 22:
            levelboard.game_over()
            game_is_on = False

    #Detected successful crossing
    if schiggy.is_at_finish_line():
        schiggy.go_to_start()
        car.level_up()
        levelboard.raise_level()
        levelboard.update_levelboard()

screen.exitonclick()
