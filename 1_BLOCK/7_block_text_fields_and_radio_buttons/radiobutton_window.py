from tkinter import *
def newtext (event):
    if prap1.get()==1 and prap4.get()==1:
        label ["text"]="Ви вибрали жовту гуаш"
        
    elif prap2.get()==1 and prap3.get()==1:
        label ["text"]="Ви вибрали зелену акварель"

    elif prap1.get()==1 and prap3.get()==1:
        label ["text"]="Ви вибрали жовту акварель"

    elif prap2.get()==1 and prap4.get()==1:
        label ["text"]="Ви вибрали зелену гуаш"

Window=Tk()
Window.geometry("400x400")
label=Label (Window, text="Не вибрано")
label.place ( x = 100 , y = 50 )
prap1=IntVar()
prap2=IntVar()
prap3=IntVar()
prap4=IntVar()

prapor1=Checkbutton (Window, text="Жовтий", variable=prap1, onvalue=1, offvalue=0)
prapor1.place ( x = 100 , y = 100 )

prapor2=Checkbutton (Window, onvalue=1, offvalue=0, text="Зелений", variable=prap2,)

prapor2.place ( x = 100 , y = 120 )
prapor3=Checkbutton (Window, text="Акварель ", variable=prap3, onvalue=1, offvalue=0)
prapor3.place (x=100, y=160)
prapor4=Checkbutton (Window, onvalue=1, offvalue=0, text="Гуаш", variable=prap4,)

prapor4.place (x=100, y=180)
label.bind("<Button-1>", newtext)
Window.mainloop()
