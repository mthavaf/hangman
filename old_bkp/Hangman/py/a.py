from tkinter import *

master = Tk()

w = Canvas(master, width=500, height=500)
w.pack()

w.create_line(150,450,150,150, fill="#476042", width=4)
w.create_line(300,150,150,150, fill="#476042", width=4)
w.create_line(100,450,200,450, fill="#476042", width=4)
w.create_line(300,150,300,200, fill="#476042", width=4)
w.create_oval(270,200,330,250, fill="#476042", width=4)
w.create_oval(285,220,289,227, fill="#476042", width=4)
w.create_oval(315,220,319,227, fill="#476042", width=4)
w.create_oval(298,225,305,232, fill="#476042", width=4)
w.create_line(290,240,310,240, fill="#476042", width=4)
w.create_line(300,300,250,250, fill="#476042", width=4)
w.create_line(300,250,300,350, fill="#476042", width=4)
w.create_line(300,300,350,250, fill="#476042", width=4)
w.create_line(300,350,250,400, fill="#476042", width=4)
w.create_line(300,350,350,400, fill="#476042", width=4)

mainloop()
