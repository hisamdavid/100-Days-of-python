from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PRIMERY = "#3C486B"
SECONDRY1 = "#F0F0F0"
SECONDRY2 = "#F9D949"
SECONDRY3 = "#F45050"
FONT_NAME = "Courier"
WORK_MIN = .025
SHORT_BREAK_MIN = .05
LONG_BREAK_MIN = .020
reps=0
timer_obj=None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
  global reps
  window.after_cancel(timer_obj)
  canvas.itemconfig(timer_text,text="00:00")
  timer.config(text="Timer")
  mark.config(text="")
  reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global reps
  reps += 1
  if reps % 8 == 0:
    count=LONG_BREAK_MIN*60
    timer.config(text="BREAK",fg=SECONDRY1)
  elif reps % 2 == 0:
    count=SHORT_BREAK_MIN*60
    timer.config(text="BREAK",fg=SECONDRY2)
  else:
    count=WORK_MIN*60
    timer.config(text="WORK",fg=SECONDRY3)
  count_down(count)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
  global timer_obj
  min=math.floor(count / 60)
  sec=count % 60
  if sec < 10:
    sec = f"0{sec}"
  time_left=f"{min}:{sec}"
  canvas.itemconfig(timer_text,text=time_left)
  if count > 0:
    timer_obj=window.after(1000,count_down,count-1)
  else:
    start_timer()
    if reps % 2 == 0:
      mark.config(text=mark.cget("text") + "✓")
    
  
# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=PRIMERY)


#timer
timer=Label(text="Timer",font=(FONT_NAME,40,"bold"),fg=SECONDRY2,bg=PRIMERY)
timer.grid(column=1,row=0)

#btns
start_btn=Button(width=10,text="Start",highlightthickness=0,command=start_timer,bg=SECONDRY1)
reset_btn=Button(width=10,text="Reset",highlightthickness=0,command=reset_timer,bg=SECONDRY1)
start_btn.grid(column=0,row=2)
reset_btn.grid(column=2,row=2)

#check-mark
mark=Label(font=(FONT_NAME,20,"bold"),fg=SECONDRY2,bg=PRIMERY)
mark.grid(column=1,row=3)

#img
canvas=Canvas(width=200,height=224,bg=PRIMERY,highlightthickness=0)
img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)



window.mainloop()
