from turtle import  Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
#You can change the keys to wasd according to your preference

game_over= False

while not game_over:
    screen.update()
    time.sleep(0.09)
    snake.move()

    #detects when the snake has made contact and ate the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    snake_head_x = snake.head.xcor()
    snake_head_y = snake.head.ycor()

    #detects when the snake has hit a wall
    if snake_head_x > 280 or snake_head_x < -280 or snake_head_y > 280 or snake_head_y < -280:
        scoreboard.reset()
        time.sleep(1)
        snake.reset()
        with open("high_scores.txt", mode="w") as file:
            file.write(f"{scoreboard.highscore}")

    #detects when the snakes head hits its own body
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            time.sleep(1)
            snake.reset()

    with open("high_scores.txt", mode="w") as file:
        file.write(f"{scoreboard.highscore}")



screen.exitonclick()
