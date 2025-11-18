from tkinter import *

a = Tk()
a.title("світлофор")
a.geometry("500x500")

c = Canvas(a, width=500, height=500, bg="white")
c.place(x=0, y=0)

c.create_rectangle([120, 100], [280, 460], fill="#7C7C7C", width=0)

c.create_polygon([200, 30], [80, 100], [320, 100], fill="#626262",width=0)
c.create_oval([150,120],[250,220],fill="#32be2b",width=0 )
c.create_oval([150,230],[250,330],fill="#d5e612",width=0 )
c.create_oval([150,340],[250,440],fill="#ea0606",width=0 )


a.mainloop()
