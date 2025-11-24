from tkinter import*
def change ( event ):
    a.geometry("300x200")
    a["bg"]="yellow"
    a.title("Оксана Когут")

    a.minsize(200,100)
    a.maxsize(1000,900)

a=Tk()
a.title("Ім'я")
a.bind("<KeyPress>", change)
a.mainloop()