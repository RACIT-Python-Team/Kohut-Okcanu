from tkinter import*
a=Tk()
a.title("Вікно №l")
a.geometry("500x500")
a.resizable(0,0)
d=Label(  a, text="Це вікно було створено в середовищі IDLE", bg="blue", fg="white", font="Arial 14"  )
d.place(x=25, y=225)

a.mainloop()