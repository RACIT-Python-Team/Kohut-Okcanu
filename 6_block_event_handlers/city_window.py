from tkinter import*
def change ( event ):
    a.geometry("400x300")
    a["bg"]="green"
    a.title("Рівне")

a=Tk()
a.title("Місто")
a.bind("<Button-1>", change)
a.mainloop()