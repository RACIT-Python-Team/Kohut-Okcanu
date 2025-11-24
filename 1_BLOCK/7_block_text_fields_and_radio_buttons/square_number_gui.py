from tkinter import*
from tkinter import messagebox
def change ( event ):
    s=int(e.get())
    r=s*s
    messagebox.showinfo("добуток", f"Добуток числа на нього самого: {r}")
    
a=Tk()
a.title("Це є вікно :)")
a.geometry("875x578")
a["bg"]="#BD5252"
a.resizable(0,0)

e=Entry(a, bg="white", width="35", font="Calibri 13") 
e.place(x=100,y=100)

b=Button(a, bg="white", text="Ок", fg="black", font="Calibri 13")
b.place(x=100, y=140)

l=Label(a, text="Введіть ціле число", bg="white", fg="black", font="Calibri 13")
l.place(x=100,y=50)

b.bind("<Button-3>",change)
a.mainloop()