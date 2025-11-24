from tkinter import*
def change ( event ):
    d=Label(  a, text="Функція виконана", bg="green", fg="white", font="Calibri 14"  )
    d.place(x=225, y=225)
a=Tk()
a.title("Вікно №2")
a.geometry("500x500")
a.resizable(0,0)


a.bind("<KeyPress>",change)
a.mainloop()