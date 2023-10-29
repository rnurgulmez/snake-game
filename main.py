# from turtle import Turtle, Screen
# we modify this and remove Turtle class because we are not going to use it in this file anymore
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
# set the tracer to off 0 and 1 means on
screen.tracer(0)

# When we create the snake example from the Snake class, we create 3 square at a time,
# that is, the snake, because these are included in the init function in the Snake class.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # we set it tracer to off,so we need to update screen to see what changed
    # we call the update here because we wanted to
    # see our all 3 squares as a one while they're moving forward
    screen.update()
    # it adds 0.1 second delay after each segment moves
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        # every time we ate the food snake will be extend.
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        # if head collides with any segment in the tail:
        # trigger game_over
        if snake.head.distance(segment) >= 10:
            continue
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
