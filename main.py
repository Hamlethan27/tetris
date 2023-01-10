# from tkinter import ttk
# from tkinter import *
# from constants import *
#
# window = Tk()
# window.title(TITLE)
# window.geometry(f"{WIDTH+40}x{HEIGHT+40}")
# window.configure()
# # window.resizable(False, False)
# s = ttk.Style()
# s.configure('game', background="#B2DFDB")
# gameFrame = ttk.Frame(master=window, width=WIDTH, height=HEIGHT, padding=20)
# gameFrame.configure(style='game')
#
#
# canvas = Canvas(master=gameFrame, width=WIDTH, height=HEIGHT, bg='lime', highlightthickness=0)
# grid = [canvas.create_rectangle(x * SIZE_OF_CELL, y * SIZE_OF_CELL, (x+1) * SIZE_OF_CELL, (y+1) * SIZE_OF_CELL, fill="white") for x in range(ROWS) for y in range(COLUMNS)]
# score = 0
# record = 0
# canvas.create_text(330, 30, text="TETRIS", fill='black', font=('aerial', 45), anchor=NW)
# canvas.create_text(400, 400, text="SCORE", fill='black', font=('aerial', 15), anchor=NW)
# canvas.create_text(400, 450, text=score, fill='black', font=('aerial', 15), anchor=NW)
# canvas.create_text(385, 600, text="BEST SCORE", fill='black', font=('aerial', 15), anchor=NW)
# canvas.create_text(385, 650, text=record, fill='black', font=('aerial', 15), anchor=NW)
#
# # print(grid.configure(bg="yellow"))
# gameFrame.pack()
# canvas.pack()
# window.mainloop()

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("500x500")
s = ttk.Style()
s.configure(style='my.frame', background='#000000', padding=10, foreground="#ffffff")
ttk.Style().configure(".", font="helvetica 13", foreground="#004D40", padding=8, background="#B2DFDB")

frame = ttk.Frame(master=root, width=500, height=500, style=s.configure('my.framed'))
ttk.Label(master=frame, text="Hello World!").pack(anchor=NW, padx=6, pady=6)
ttk.Label(master=frame, text="Hello World!").pack(anchor=NW, padx=6, pady=6)


root.mainloop()