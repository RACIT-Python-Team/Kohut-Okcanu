from tkinter import*

def change ( event ):
    a.geometry("400x300")
    a["bg"]="green"
    a.title("Вікно №2")
    a.minsize(400,500)
    a.maxsize(900,1000)
a=Tk()
a.title("Вікно №1")
a.geometry("700x400")
a["bg"]="red"
a.bind("<Button-1>", change)
a.mainloop()
