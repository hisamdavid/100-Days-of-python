import turtle
import pandas

data=pandas.read_csv("50_states.csv")

screen=turtle.Screen()
screen.title("U.S states game")
img="blank_states_img.gif"
screen.addshape(img)
screen.setup(width=750,height=500)

turtle.shape(img)
writer=turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.speed("fastest")

def printState(state_name):
  global data
  state=data[data["state"] == state_name]
  x_vlaue=int(state["x"].tolist()[0])
  y_value=int(state["y"].tolist()[0])
  writer.goto(x_vlaue,y_value)
  writer.write(state_name,align="center",font=("Arial",12,"bold"))
  index = int(data.index[data['state'] == state_name].tolist()[0])
  data=data.drop(index)


game_is_on=True
while game_is_on:

  answer_state= screen.textinput(title="guess the state",prompt="what's another state")
  name_is_there= answer_state.title() in data["state"].tolist()
  if name_is_there:
    printState(answer_state)
  if len(data) == 0:
    game_is_on=False


turtle.mainloop()

