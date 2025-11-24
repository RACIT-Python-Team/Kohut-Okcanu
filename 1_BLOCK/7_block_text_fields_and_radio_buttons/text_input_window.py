from tkinter import*
def change ( event ):
    l["text"]=e.get()

a=Tk()
a.title("Вікно №3")
a.geometry("600x700")
a["bg"]="#BD5252"
a.resizable(0,0)

e=Entry(a, bg="white", width="30", font="Calibri 13") 
e.place(x=180,y=350)

b=Button(a, bg="white", text="Ок", fg="black", font="Calibri 13")
b.place(x=300, y=400)

l=Label(a, text="Ви нічого не ввели", bg="white", fg="black", font="Calibri 13")
l.place(x=250,y=300)

b.bind("<Button-3>",change)
a.mainloop()