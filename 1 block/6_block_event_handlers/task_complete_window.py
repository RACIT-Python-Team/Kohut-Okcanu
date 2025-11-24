from tkinter import*
from tkinter import messagebox
def change ( event ):
    a.geometry("560x435")
    but.place(x=240, y=217)
    a["bg"]="yellow"
    a.title("Завдання виконано!")
    messagebox.showinfo("Виконано","Зміни застосовані!")
    
a=Tk()
but=Button(a, bg="pink", text="Змінити", fg="blue")
but.place(x=225, y=225)
a.title("Це вікно Python")
a.geometry("500x500")
a["bg"]="red"
but.bind("<Button-3>", change)
a.mainloop()
