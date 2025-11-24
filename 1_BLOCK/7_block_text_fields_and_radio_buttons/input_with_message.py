from tkinter import*
from tkinter import messagebox
def change ( event ):
    l["text"]=e.get()
    messagebox.showinfo("Підтвердження події","Дія виконана!")
a=Tk()
a.title("Перше вікно")
a.geometry("600x600")
a["bg"]="#94960C"
a.resizable(0,0)

e=Entry(a, bg="white", width="30", font="Calibri 12") 
e.place(x=180,y=350)

l=Label(a, text="Ви нічого не ввели", bg="#C19494", fg="#150A76", font="Calibri 12")
l.place(x=250,y=300)

a.bind("<Button-3>",change)
a.mainloop()