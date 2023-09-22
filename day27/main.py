from tkinter import *

def milToKm():
  mil = float(mil_input.get())
  km= round(mil * 1.609)
  text_lable.config(text=f"is equal to      {km}      km")

window=Tk()
window.title("mil to km")
window.config(padx=20,pady=20)

mil_input=Entry(width=10)
mil_input.grid(column=1,row=0)
mil_lable=Label(text="Miles", padx=10)
mil_lable.grid(column=2,row=0)
text_lable=Label(text=f"is equal to      {0}      km")
text_lable.grid(row=1,column=0)
calc_btn=Button(text='calculate',command=milToKm)
calc_btn.grid(row=2,column=1)








window.mainloop()

