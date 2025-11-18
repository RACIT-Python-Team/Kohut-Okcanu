from tkinter import *
from tkinter import messagebox
def newtext (event):
    if p1.get()==1 and p3.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали ванільне морозиво з шоколадной присипкой")

    elif p1.get()==1 and p4.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали ванільне морозиво з кокосовой стружкой")

    elif p2.get()==1 and p3.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали шоколадне морозиво з шоколадной присипкой")

    elif p2.get()==1 and p4.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали шоколадне морозиво з кокосовой стружкой")

    elif p5.get()==1 and p3.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали фруктове морозиво з шоколадной присипкой")

    elif p5.get()==1 and p4.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали фруктове морозиво з кокосовой стружкой")

    
a=Tk()
a.geometry("400x400")
a.title("Магазин морозива 2")
l=Label (a, text="Оберіть тип морозива")
l.place ( x = 100 , y = 80 )
l1=Label (a, text="Оберіть тип присипки")
l1.place ( x = 100 , y = 180 )
p1=IntVar()
p2=IntVar()
p3=IntVar()
p4=IntVar()
p5=IntVar()
p6=IntVar()


pr1=Checkbutton (a, text="Ванільне", variable=p1, onvalue=1, offvalue=0)
pr1.place ( x = 100 , y = 100 )

pr2=Checkbutton (a, onvalue=1, offvalue=0, text="Шоколадне", variable=p2,)
pr2.place ( x = 100 , y = 120 )
pr5=Checkbutton (a, onvalue=1, offvalue=0, text="Фруктове", variable=p5,)
pr5.place ( x = 100 , y = 140 )

pr3=Checkbutton (a, text="шоколадна присипка", variable=p3, onvalue=1, offvalue=0)
pr3.place (x=100, y=200)

pr4=Checkbutton (a, onvalue=1, offvalue=0, text="кокосова стружка", variable=p4,)
pr4.place (x=100, y=220)


b=Button(a, bg="white", text="Ок", fg="black", font="Calibri 13",)
b.place(x=100, y=260)

b.bind("<Button-1>", newtext)
a.mainloop()
