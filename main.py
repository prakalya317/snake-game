from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My snake game")
my_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(key="Up", fun=snake.up)
my_screen.onkey(key="Down", fun=snake.down)
my_screen.onkey(key="Right", fun=snake.right)
my_screen.onkey(key="Left", fun=snake.left)

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with wall.
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() < -295 or snake.head.ycor() > 295:
        game_is_on = False
        scoreboard.game_over()
        time.sleep(2.0)
        scoreboard.reset()
        snake.reset()
        game_is_on = True

        # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.clear()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            time.sleep(2.0)
            scoreboard.reset()
            snake.reset()
            game_is_on = True

my_screen.exitonclick()
