from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
screen=Screen()
screen.bgcolor("black")
screen.title("pong")
screen.setup(width=800,height=600)
screen.tracer(0)


right_player=Paddle(360,0)
left_player=Paddle(-360,0)
ball=Ball()
score_board = Score()

screen.listen()
screen.onkey(right_player.go_up,"Up")
screen.onkey(right_player.go_down,"Down")
screen.onkey(left_player.go_up,"w")
screen.onkey(left_player.go_down,"s")

game_is_on=True

while game_is_on:
  time.sleep(ball.movspeed)
  screen.update()
  ball.move()
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounceOnWall()
  x_pos=ball.xcor()
  r_pos=ball.distance(right_player.player)
  l_pos=ball.distance(left_player.player)
  if (x_pos > 350 or x_pos < -350):
    if (r_pos < 59 or l_pos < 59) :
      ball.bounceOnPaddle()
    else:
      ball.resetPos()
      if (x_pos > 350):
        score_board.l_score += 1
      elif (x_pos < -350):
        score_board.r_score += 1
      score_board.updateScore()



screen.exitonclick()