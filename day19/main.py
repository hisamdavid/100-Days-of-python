from turtle import Turtle, Screen
import random
isRaceOn=False
screen = Screen()
screen.setup(width=500,height=400)
user_input=screen.textinput(title="make your choice",prompt="witch turtle will win?")

colors=["red","orange","yellow","green","blue","purple"]
candites=[]
y=-70

for turtleNum in range(0,6):
  david=Turtle(shape="turtle")
  david.color(colors[turtleNum])
  david.penup()
  david.goto(x=-230,y=y)
  y+=30
  candites.append(david)

if user_input:
  isRaceOn=True

while isRaceOn:
  for turtle in candites:
    if turtle.xcor() > 230:
      isRaceOn=False
      winer=turtle.pencolor()
      if winer == user_input:
        print("you've won")
      else:
        print("that is a lose my brother")
      break
    turtle.forward(random.randint(0,10))
    

screen.exitonclick()