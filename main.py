import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Score()

screen.listen()
screen.onkeypress(player.move, "w")

game_is_on = True
counter = 0
level = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if not counter % 5:
        car_manager.create_car()
    car_manager.move_cars(score.score)
    counter += 1
    if player.ycor() > 280:
        player.reset_position()
        score.increment()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()
