from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
screen.listen()


snake = Snake()
food = Food()
screen.update()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:

    screen.update()
    snake.snake_move()

    epsilon = 0.0001
    if abs(snake.turtle_zoo[0].xcor() - food.xcor()) < epsilon and abs(snake.turtle_zoo[0].ycor() - food.ycor()) < epsilon:

        snake.grow()
        food.refresh()
        scoreboard.get_score()

    #detect collision with wall
    if snake.turtle_zoo[0].xcor() > 290  or snake.turtle_zoo[0].ycor() > 290 or snake.turtle_zoo[0].xcor() < -290 or snake.turtle_zoo[0].ycor() < -290:
        #game_is_on = False
        scoreboard.reset_score()
        snake.reset_snake()
        print("you lose")

    #detect collision with tail
    # for i in range(1,len(snake.turtle_zoo)):
    #
    #     if snake.turtle_zoo[0].distance(snake.turtle_zoo[i]) <10:
    #         game_is_on = False
    #         scoreboard.game_over()
    #         print("you lose")

    for segment in snake.turtle_zoo[1:]:
        # if segment == snake.turtle_zoo[0]:
        #     pass
        if snake.turtle_zoo[0].distance(segment) < 10:
            #game_is_on = False
            scoreboard.reset_score()
            snake.reset_snake()
            print("you lose")



    screen.listen()
    screen.onkeypress(fun=snake.turn_left, key="a")
    screen.onkeypress(fun=snake.turn_right, key="d")













screen.exitonclick()