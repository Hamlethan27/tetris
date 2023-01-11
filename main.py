# from tkinter import *
# from tkinter import Canvas, messagebox
# from random import *
# from constants import *
# from random import choice
# import copy
# import time
# def on_closing():
#     global app_running
#     if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
#         app_running = False
#
#
# app_running = True
# window = Tk()
# window.title(TITLE)
# window.geometry(f"{WIDTH}x{HEIGHT}")
# window.resizable(False, False)
# gameFrame = Frame(window, bg="lime", padx=50, pady=20)
# gameFrame.pack()
# tetris = Canvas(gameFrame, height=COLUMNS * SIZE_OF_CELL + 1, width=ROWS * SIZE_OF_CELL + 1, bg=BG_COLOUR, highlightthickness=0)
# tetris.pack()
# grid = [tetris.create_rectangle(x * SIZE_OF_CELL, y * SIZE_OF_CELL, (x + 1) * SIZE_OF_CELL, (y + 1) * SIZE_OF_CELL) for x in range(ROWS) for y in range(COLUMNS)]
#
# shapes = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],  # I
#           [(0, -1), (-1, -1), (-1, 0), (0, 0)],  # O
#           [(-1, 0), (-1, 1), (0, 0), (0, -1)],  # S
#           [(0, 0), (-1, 0), (0, 1), (-1, -1)],  # Z
#           [(0, 0), (0, -1), (0, 1), (-1, -1)],  # J
#           [(0, 0), (0, -1), (0, 1), (1, -1)],  # L
#           [(0, 0), (0, -1), (0, 1), (-1, 0)]]  # T
#
# shapesOnGrid = [[[x + ROWS // 2, y + 1, 1, 1] for x, y in figPos] for figPos in shapes]
# field = [[0] * ROWS for i in range(COLUMNS)]
#
# anim_count, anim_speed, anim_limit = 0, 60, 2000
# dx, rotate = 0, False
#
#
# def rgbToHex(color:[]):
#     return "#" + '{:x}{:x}{:x}'.format(color[0], color[1], color[2])
#
#
# def getRandomColor():
#     return randrange(30, 255), randrange(30, 255), randrange(30, 255)
#
#
# def check_borders():
#     for i in range(len(shape)):
#         if shape[i][0] < 0 or shape[i][0] > ROWS - 1:
#             return False
#         elif shape[i][1] > COLUMNS - 1 or field[shape[i][1]][shape[i][0]]:
#             return False
#     return True
#
#
# def move(arrow):
#     global rotate, anim_limit, dx
#     if arrow.keysym == 'Up':
#         rotate = True
#     elif arrow.keysym == 'Down':
#         anim_limit = 100
#     elif arrow.keysym == 'Left':
#         dx = -1
#     elif arrow.keysym == 'Right':
#         dx = 1
#
#
# tetris.bind_all("<KeyPress-Up>", move)
# tetris.bind_all("<KeyPress-Down>", move)
# tetris.bind_all("<KeyPress-Left>", move)
# tetris.bind_all("<KeyPress-Right>", move)
#
# shape = list(copy.deepcopy(choice(shapesOnGrid)))
# print(type(shape[0][0]))
# color = getRandomColor()
#
#
# while app_running:
#     if app_running:
#
#
#         fig = []
#         # draw figure
#         for i in range(4):
#             horizontal = shape[i][0] * SIZE_OF_CELL
#             vertical = shape[i][1] * SIZE_OF_CELL
#             fig.append(
#                 tetris.create_rectangle(horizontal, vertical, horizontal + SIZE_OF_CELL, vertical + SIZE_OF_CELL,
#                                         fill=rgbToHex(color)))
#
#
#         # move x
#         previousShape = list(copy.deepcopy(shape))
#         for i in range(4):
#             shape[i][0] = shape[i][0] + dx
#             if not check_borders():
#                 shape = list(copy.deepcopy(previousShape))
#                 break
#
#         # move y
#         anim_count += anim_speed
#         if anim_count > anim_limit:
#             anim_count = 0
#             previousShape = list(copy.deepcopy(shape))
#             for i in range(4):
#                 shape[i][1] += 1
#                 if not check_borders():
#                     for i in range(4):
#                         field[previousShape[i][1]][previousShape[i][0]] = color
#                     shape = copy.deepcopy(choice(shapes))
#                     print(shape)
#                     color = getRandomColor()
#                     anim_limit = 2000
#                     break
#
#         # rotate
#         center = shape[0]
#         previousShape = list(copy.deepcopy(shape))
#         if rotate:
#             for i in range(4):
#                 x = shape[i][1] - center[1]
#                 y = shape[i][0] - center[0]
#                 shape[i][0] = center[0] - x
#                 shape[i][1] = center[1] + y
#                 if not check_borders():
#                     shape = list(copy.deepcopy(previousShape))
#                     break
#         # check lines
#         line, lines = COLUMNS - 1, 0
#         for row in range(COLUMNS - 1, -1, -1):
#             count = 0
#             for i in range(ROWS):
#                 if field[row][i]:
#                     count += 1
#                 field[line][i] = field[row][i]
#             if count < ROWS:
#                 line -= 1
#             else:
#                 anim_speed += 3
#                 lines += 1
#
#
#
#         # draw field
#         for y, raw in enumerate(field):
#             for x, col in enumerate(raw):
#                 if col:
#                     horizontal, vertical = x * SIZE_OF_CELL, y * SIZE_OF_CELL
#                     fig.append(tetris.create_rectangle(horizontal, vertical, horizontal + SIZE_OF_CELL,
#                                                        vertical + SIZE_OF_CELL, fill=rgbToHex(col)))
#
#
#
#         # game over
#         for i in range(ROWS):
#             if field[0][i]:
#
#                 field = [[0 for i in range(ROWS)] for j in range(COLUMNS)]
#                 anim_count, anim_speed, anim_limit = 0, 60, 2000
#                 # for item in grid:
#                 #     tetris.itemconfigure(item, fill=rgbToHex(getRandomColor()))
#                 #     time.sleep(0.005)
#                 #     window.update_idletasks()
#                 #     window.update()
#                 #
#                 # for item in grid:
#                 #     tetris.itemconfigure(item, fill="")
#
#         dx, rotate = 0, False
#         window.update_idletasks()
#         window.update()
#         for id_fig in fig:
#             tetris.delete(id_fig)
#     time.sleep(0.01)
#
# window.destroy()
