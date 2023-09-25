import tkinter
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

##########- data and code -##########
try:
  data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
  data = pandas.read_csv("data/deck_words.csv")
data_dict = data.to_dict(orient="records")

def genrate_card(): 
  try:
    card_info = random.choice(data_dict)
    card_front = card_info[data.columns[0]]
    card_back = card_info[data.columns[1]]
    card_view.itemconfig(word,text=card_front,fill="black")
    card_view.itemconfig(bg_img,image=front_card)
    card_view.itemconfig(lang,fill="black")
    #please don't ask why i have a nested function 
    def flip_card():
      card_view.itemconfig(bg_img,image=back_card)
      card_view.itemconfig(lang,fill="white")
      card_view.itemconfig(word,fill="white",text=card_back)

    main_window.after(3000,flip_card)
    return card_info
  except IndexError:
    return -1


def right_answer():
  global data_dict
  item = genrate_card()
  if item == -1:
    card_view.itemconfig(bg_img,image=front_card)
    card_view.itemconfig(lang,text="Congratulations",fill="black")
    card_view.itemconfig(word,text="you just finshed the deck",fill="black")
  else:
    data_dict.remove(item)

def exit_function():
    new_data = pandas.DataFrame(data_dict)
    main_window.destroy()
    new_data.to_csv('data/words_to_learn.csv', index=False)



##########-UI-##########

#screen
main_window= tkinter.Tk()
main_window.title("Flash Cards")
main_window.config(padx=50, pady=50)
main_window.config(background=BACKGROUND_COLOR)
main_window.protocol('WM_DELETE_WINDOW', exit_function)

#buttons
right_image = tkinter.PhotoImage(file="images/right.png")
wrong_image = tkinter.PhotoImage(file="images/wrong.png")
right_btn = tkinter.Button(image=right_image, highlightthickness=0,borderwidth=0,command=right_answer)
wrong_btn = tkinter.Button(image=wrong_image, highlightthickness=0,borderwidth=0,command=genrate_card)


#card-view
front_card = tkinter.PhotoImage(file="images/card_front.png")
back_card = tkinter.PhotoImage(file="images/card_back.png")
card_view = tkinter.Canvas(height=526, width=800,background=BACKGROUND_COLOR,borderwidth=0,highlightthickness=0)
bg_img = card_view.create_image(400,263,image=front_card)
lang = card_view.create_text(400,150,text=data.columns[0],font=("Ariel",40,"italic"))
word = card_view.create_text(400,263,text="word",font=("Ariel",60,"bold"))
genrate_card()



#layout
wrong_btn.grid(column=0,row=1)
right_btn.grid(column=1,row=1)
card_view.grid(column=0,row=0,columnspan=2)

main_window.mainloop()
