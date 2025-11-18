from tkinter import *

a = Tk()
a.title("Будинок")
a.geometry("500x500")

c = Canvas(a, width=500, height=500, bg="white")
c.place(x=0, y=0)


c.create_rectangle([200, 180], [400, 380], fill="#692289", width=0)


c.create_rectangle([260, 240], [340, 300], fill="#C7C7C7", width=0)
c.create_rectangle([205, 120], [230, 180], fill="#4bd161",width=0)
c.create_line([260, 270], [340, 270], fill="black",width=2)
c.create_line([300, 240], [300, 300], fill="black",width=2)

c.create_polygon([300, 100], [170, 200], [430, 200], fill="#2667d0",width=0)



a.mainloop()

