from constants import *
from tkinter import *
from tkinter import messagebox
import random
import copy
import time


window = Tk()
window.title(TITLE)
window.resizable(False, False)


def on_closing():
    global isRunning
    if messagebox.askokcancel("App exit", "Do you want to quit the app?"):
        isRunning = False


window.protocol("WM_DELETE_WINDOW", on_closing)


gameFrame = Frame(window, width=WIDTH, height=HEIGHT, bg=BG_COLOR, highlightthickness=0)
gameFrame.pack()

tetris = Canvas(gameFrame, width=COLUMNS * SIZE_OF_CELL + 1, height=ROWS * SIZE_OF_CELL + 1, bg=TETRIS_BG_COLOR, highlightthickness=0)
tetris.pack(padx=20, pady=20)

grid = [tetris.create_rectangle(x * SIZE_OF_CELL, y * SIZE_OF_CELL, (x + 1) * SIZE_OF_CELL, (y + 1) * SIZE_OF_CELL) for x in range(COLUMNS) for y in range(ROWS)]

shapes = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],    # I
          [(0, -1), (-1, -1), (-1, 0), (0, 0)],  # O
          [(-1, 0), (-1, 1), (0, 0), (0, -1)],   # S
          [(0, 0), (-1, 0), (0, 1), (-1, -1)],   # Z
          [(0, 0), (0, -1), (0, 1), (-1, -1)],   # J
          [(0, 0), (0, -1), (0, 1), (1, -1)],    # L
          [(0, 0), (0, -1), (0, 1), (-1, 0)]]    # T

gridShapes = [[[x + COLUMNS // 2, y+1] for x, y in fig_pos] for fig_pos in shapes]        # Positions of shapes in the center of the board

squares = [[0]*COLUMNS for j in range(ROWS)]       # An array of the values of the squares on which the figures have fallen

fallCount, fallSpeed, fallDelay = 0, 60, 2000

shape = copy.deepcopy(random.choice(gridShapes))


def isBorder(shape):
    if shape[0] < 0 or shape[0] > COLUMNS - 1:
        return True
    elif shape[1] > ROWS - 1 or squares[shape[1]][shape[0]]:
        return True
    return False


def move(arrow):
    global rotate, fallDelay, X
    if arrow.keysym == 'Up':
        rotate = True
    elif arrow.keysym == 'Down':
        fallDelay = 100
    elif arrow.keysym == 'Left':
        X = -1
    elif arrow.keysym == 'Right':
        X = 1


tetris.bind_all("<KeyPress-Up>", move)
tetris.bind_all("<KeyPress-Down>", move)
tetris.bind_all("<KeyPress-Left>", move)
tetris.bind_all("<KeyPress-Right>", move)


isRunning = True
X, rotate = 0, False
while isRunning:
    if isRunning:
        previousShape = copy.deepcopy(shape)


        # horizontal movement
        for i in range(4):
            shape[i][0] += X
            if isBorder(shape[i]):
                shape = copy.deepcopy(previousShape)
                break


        # vertical movement
        fallCount += fallSpeed
        if fallCount > fallDelay:
            fallCount = 0
            previousShape = copy.deepcopy(shape)
            for i in range(4):
                shape[i][1] += 1
                if isBorder(shape[i]):
                    for j in range(4):
                        squares[previousShape[j][1]][previousShape[j][0]] = SHAPE_COLOR     #the squares where the figure fell are filled with SHAPE_COLOR
                    shape = copy.deepcopy(random.choice(gridShapes))
                    fallDelay = 2000
                    break


        # rotate clockwise
        previousShape = copy.deepcopy(shape)
        if rotate:
            center = shape[0]
            for i in range(4):
                x = shape[i][1] - center[1]
                y = shape[i][0] - center[0]
                shape[i][0] = center[0] - x     # just put the opposite sign to change the direction of rotation (counterclockwise)
                shape[i][1] = center[1] + y
                if isBorder(shape[i]):
                    shape = copy.deepcopy(previousShape)
                    break


        # check for full line
        line = ROWS - 1
        for row in range(ROWS - 1, -1, -1):
            count = 0
            for i in range(COLUMNS):
                if squares[row][i]:
                    count += 1
                squares[line][i] = squares[row][i]
            if count < COLUMNS:
                line -= 1
            else:
                fallSpeed += 3

        existingShapes = []
        # drawing shape
        for i in range(4):
            horizontal = shape[i][0] * SIZE_OF_CELL
            vertical = shape[i][1] * SIZE_OF_CELL
            existingShapes.append(tetris.create_rectangle(horizontal, vertical, horizontal + SIZE_OF_CELL, vertical + SIZE_OF_CELL, fill=SHAPE_COLOR))
            if isBorder(shape[i]):
                shape = copy.deepcopy(previousShape)
                break


        # saving color squares in grid
        for y, row in enumerate(squares):                 #enumerate returns two values - index and value
            for x, col in enumerate(row):
                if col:
                    parts = [x * SIZE_OF_CELL, y * SIZE_OF_CELL]
                    existingShapes.append(
                        tetris.create_rectangle(parts[0], parts[1], parts[0] + SIZE_OF_CELL, parts[1] + SIZE_OF_CELL,
                                                fill=SHAPE_COLOR))

        # if top line is full
        for i in range(COLUMNS):
            if squares[0][i]:
                squares = [[0] * COLUMNS for i in range(ROWS)] # to clear all squares after the tetris height overflow
                fallCount, fallSpeed, fallDelay = 0, 60, 2000
                for item in grid:
                    tetris.itemconfigure(item, fill=TETRIS_BG_COLOR)  # to fill all squares with this color after the tetris height overflow

        X, rotate = 0, False
        window.update_idletasks()
        window.update()
        for i in existingShapes:
            tetris.delete(i)                # удаление фигур из existingShapes, чтобы не повторялось
    time.sleep(0.005)


window.destroy()
