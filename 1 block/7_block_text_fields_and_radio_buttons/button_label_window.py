from tkinter import*
def change ( event ):
    d=Label(  a, text="Це вікно було створено в середовищі IDLE", bg="blue", fg="white", font="Arial 14"  )
    d.place(x=200, y=250)
    a["bg"]="blue" \
    
a=Tk()
a.title("Вікно №3")
a.geometry("500x500")
b=Button(a, bg="blue", text="Розфарбуй", fg="black")
b.place(x=200, y=200)

a.resizable(0,0)


b.bind("<Button-3>",change)
a.mainloop()