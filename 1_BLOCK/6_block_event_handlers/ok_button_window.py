from tkinter import*

def change ( event ):
    a.geometry("650x560")
    a["bg"]="purple"
    a.title("Завдання виконано!")
    but=Button(a, bg="yellow", text="Ok", fg="black")
    
a=Tk()
but=Button(a, bg="purple", text="Ok", fg="black")
but.place(x=200, y=390)
a.title("Вікно №2")
a.geometry("500x800")
a["bg"]="red"
but.bind("<Button-1>", change)
a.mainloop()
