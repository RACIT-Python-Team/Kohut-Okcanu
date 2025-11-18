from tkinter import *

a = Tk()
a.title("смайлик")
a.geometry("500x500")

c = Canvas(a, width=500, height=500, bg="white")
c.place(x=0, y=0)

c.create_oval([9,140],[300,440],fill="#fde800",width=2, outline="#fd3b00")

c.create_polygon([160, 380], [65, 350], [250, 350], fill="#DD9F42",width=2, outline="#66460f")

c.create_rectangle([152, 285], [168, 325], fill="#38387f",width=0)

c.create_oval([180,270],[230,220],fill="#c5c5c5",width=2 )
c.create_oval([205,265],[225,245],fill="#000000",width=2 )

c.create_oval([80,270],[130,220],fill="#c5c5c5",width=2 )
c.create_oval([105,265],[125,245],fill="#000000",width=2 )

a.mainloop()