from tkinter import*

def change ( event ):
    a.geometry("650x560")
    a["bg"]="green"
    a.title("Вікно №2")
    but=Button(a, bg="bloo", text="Розфарбуй", fg="black")
a=Tk()
but=Button(a, bg="yellow", text="Розфарбуй", fg="black")
but.place(x=100, y=90)
a.title("Вікно №1")
a.geometry("400x300")
a["bg"]="red"
but.bind("<Button-1>", change)
a.mainloop()
