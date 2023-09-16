from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake")
screen.tracer(0)


snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while(game_is_on):
  screen.update()
  time.sleep(.05)
  snake.move()
  if snake.head.distance(food) < 15:
    food.refresh()
    scoreboard.refresh_score()
    snake.extend()

  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    game_is_on=False
    scoreboard.game_over()

  for seg in snake.segments[1:]:
    if snake.head.distance(seg) < 10:
      game_is_on=False
      scoreboard.game_over()

    
screen.exitonclick()