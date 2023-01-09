from tkinter import *
from tkinter import ttk, Canvas
import tkinter as tk
from random import *
from constants import *
from random import choice
from copy import deepcopy


window = Tk()
window.title(TITLE)
window.geometry(f"{WIDTH}x{HEIGHT}")




gameFrame = Frame(window, bg="yellow", padx=50, pady=20)


tetrisFrame = Frame(gameFrame)
tetris = Canvas(tetrisFrame, height=COLUMNS * SIZE_OF_CELL + 1, width=ROWS * SIZE_OF_CELL + 1, bg=BG_COLOUR, highlightthickness=0)
grid = [tetris.create_rectangle(x*SIZE_OF_CELL, y*SIZE_OF_CELL, (x+1)*SIZE_OF_CELL, (y+1)*SIZE_OF_CELL) for x in range(ROWS) for y in range(COLUMNS)]


infoFrame = Frame(gameFrame, height= 600, width=WIDTH-320, highlightthickness=20)
score = 0
record = 0
scoreLabelText = Label(infoFrame, text="Score: ", font=[FONT_FAMILY, FONT_SIZE]).pack(pady=10)
scoreLabel = Label(infoFrame, text = score, font=[FONT_FAMILY, FONT_SIZE]).pack(pady=30)
recordLabelText = Label(infoFrame, text="Record: ", font=[FONT_FAMILY, FONT_SIZE]).pack(pady=10)
recordLabel = Label(infoFrame, text = score, font=[FONT_FAMILY, FONT_SIZE]).pack(pady=30)


shapes = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
         [(0, -1), (-1, -1), (-1, 0), (0, 0)],
         [(-1, 0), (-1, 1), (0, 0), (0, -1)],
         [(0, 0), (-1, 0), (0, 1), (-1, -1)],
         [(0, 0), (0, -1), (0, 1), (-1, -1)],
         [(0, 0), (0, -1), (0, 1), (1, -1)],
         [(0, 0), (0, -1), (0, 1), (-1, 0)]]

shapesOnGrid = [[[x + ROWS // 2, y + 1, 1, 1] for x, y in figPos] for figPos in shapes]

shape, nextShape = deepcopy(choice(shapesOnGrid)), deepcopy(choice(shapesOnGrid))
# color = randrange(0, 255) * randrange(0, 255)

for i in range(4):
    horizontalPart = shape[i][0] * SIZE_OF_CELL
    verticalPart = shape[i][1] * SIZE_OF_CELL
    tetris.create_rectangle(horizontalPart, verticalPart, horizontalPart + SIZE_OF_CELL, verticalPart + SIZE_OF_CELL, fill="green")

gameFrame.pack()
tetrisFrame.pack(side=LEFT)
tetris.pack()
infoFrame.pack(side=RIGHT, padx=10)

window.mainloop()