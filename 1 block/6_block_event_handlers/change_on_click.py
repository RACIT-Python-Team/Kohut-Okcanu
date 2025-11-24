from tkinter import*
def change ( event ):
    a.geometry("700x600")
    a["bg"]="violet"
    a.title("РФКІТ")
    a.resizable(0,0)

a=Tk()
a.title("коледж")
a.bind("<Button-3>", change)
a.mainloop()