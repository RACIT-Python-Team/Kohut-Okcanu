from tkinter import*
from tkinter import messagebox
def change ( event ):
    a.geometry("500x600")
    a["bg"]="gray"
    a.title("ІПЗ-2/2")
    a.minsize(400,500)
    a.maxsize(900,1000)
a=Tk()
a.title("група")
def mmm(event):
   messagebox.showinfo("клас","Я навчаюся у 8 класі!")


a.bind("<KeyPress>", change)
a.bind("<Button-1>", mmm)
a.mainloop()

