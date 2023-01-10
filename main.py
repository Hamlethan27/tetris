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
tetris = Canvas(tetrisFrame, height=COLUMNS * SIZE_OF_CELL + 1, width=ROWS * SIZE_OF_CELL + 1, bg=BG_COLOUR,
                highlightthickness=0)
grid = [tetris.create_rectangle(x * SIZE_OF_CELL, y * SIZE_OF_CELL, (x + 1) * SIZE_OF_CELL, (y + 1) * SIZE_OF_CELL) for
        x in range(ROWS) for y in range(COLUMNS)]

infoFrame = Frame(gameFrame, height=600, width=WIDTH - 320, highlightthickness=20)
score = 0
record = 0
scoreFrame = Frame(infoFrame)
recordFrame = Frame(infoFrame)
nextShapeFrame = Frame(infoFrame)
nextShapeGrid = Canvas(nextShapeFrame, width=SIZE_OF_CELL * 4, height=SIZE_OF_CELL * 4)
Label(scoreFrame, text="Score: ", font=[FONT_FAMILY, FONT_SIZE]).pack()
Label(scoreFrame, text=score, font=[FONT_FAMILY, FONT_SIZE]).pack()
Label(recordFrame, text="Record: ", font=[FONT_FAMILY, FONT_SIZE]).pack()
Label(recordFrame, text=score, font=[FONT_FAMILY, FONT_SIZE]).pack()

shapes = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],  # I
          [(0, -1), (-1, -1), (-1, 0), (0, 0)],  # O
          [(-1, 0), (-1, 1), (0, 0), (0, -1)],  # S
          [(0, 0), (-1, 0), (0, 1), (-1, -1)],  # Z
          [(0, 0), (0, -1), (0, 1), (-1, -1)],  # J
          [(0, 0), (0, -1), (0, 1), (1, -1)],  # L
          [(0, 0), (0, -1), (0, 1), (-1, 0)]]  # T

shapesOnGrid = [[[x + ROWS // 2, y + 1, 1, 1] for x, y in figPos] for figPos in shapes]


def rgb_to_hex(r, g, b):
    return '#' + '{:X}{:X}{:X}'.format(r, g, b)


shape, nextShape = deepcopy(choice(shapesOnGrid)), deepcopy(choice(shapesOnGrid))
red = round(randrange(20, 255))
green = round(randrange(20, 255))
blue = round(randrange(20, 255))
color = rgb_to_hex(red, green, blue)

gameFrame.pack()
tetrisFrame.pack(side=LEFT)
tetris.pack()
infoFrame.pack(side=RIGHT, padx=10)
scoreFrame.pack(pady=20)
recordFrame.pack(pady=20)

while (True):

    for i in range(4):
        horizontalPart = shape[i][0] * SIZE_OF_CELL
        verticalPart = shape[i][1] * SIZE_OF_CELL
        tetris.create_rectangle(horizontalPart, verticalPart, horizontalPart + SIZE_OF_CELL,
                                verticalPart + SIZE_OF_CELL,
                                fill=color)
    down = 0
    while(down != COLUMNS):
        horizontalPart = shape[i][0] * SIZE_OF_CELL + down
        verticalPart = shape[i][1] * SIZE_OF_CELL
        tetris.create_rectangle(horizontalPart, verticalPart, horizontalPart + SIZE_OF_CELL,
                                verticalPart + SIZE_OF_CELL,
                                fill=BG_COLOUR)
        down += 1
        horizontalPart = shape[i][0] * SIZE_OF_CELL + down
        verticalPart = shape[i][1] * SIZE_OF_CELL
        tetris.create_rectangle(horizontalPart, verticalPart, horizontalPart + SIZE_OF_CELL,
                                verticalPart + SIZE_OF_CELL,
                                fill=color)


window.mainloop()
