from tkinter import *

def submit():
    label = Label(text=f"temperature is {scale.get()} cenlious")
    label.pack()
window = Tk()

hotImage = PhotoImage(file='flame.png')
hotImage = hotImage.subsample(2,2)
hotImage = hotImage.subsample(2,2)
hotImage = hotImage.subsample(2,2)
hotLabel = Label(image=hotImage).pack()

scale = Scale(window,from_=100,to=0,length=400,orient=VERTICAL,font=("Consolas",20),tickinterval_=10
              ,showvalue =0,
              resolution=5,
              troughcolor='#69EAFF',fg="#FF1C00",bg="black",
              )

scale.set(((scale["from"]-scale["to"])/2)+scale["to"])

scale.pack()

coldImage = PhotoImage(file="snowflake.png")
coldImage = coldImage.subsample(2,2)
coldLabel = Label(image=coldImage).pack()

button = Button(window,text='submit',command=submit).pack()

window.mainloop()