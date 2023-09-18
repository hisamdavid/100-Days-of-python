from turtle import Turtle

class Paddle():
  def __init__(self,x,y) :
    self.player=Turtle("square")
    self.player.color("white")
    self.player.shapesize(stretch_len=1,stretch_wid=5)
    self.player.penup()
    self.player.goto(x,y)
  
  def go_up(self):
    if self.player.ycor() > 210:
      return
    self.player.goto(self.player.xcor(),self.player.ycor()+20)

  def go_down(self):
    if self.player.ycor() < -210:
      return
    self.player.goto(self.player.xcor(),self.player.ycor()-20)
