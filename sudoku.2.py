import pygame as pg
import numpy as np
import random

WIDTH = 550
background_color = pg.Color("white")

board = [
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0]
]

current = [
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0]
]

def insert(win, position):
	global current, board
	i,j = position[1], position[0]
	buffer = 5
	font = pg.font.SysFont("Comic Sans MS", 35)
	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				return
			if event.type == pg.KEYDOWN:
				if board[i-1][j-1] != 0:
					return
				if event.key == 48:
					current[i-1][j-1] = event.key - 48
					pg.draw.rect(win, pg.Color("white"), (position[0]*50 + buffer, position[1]*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
					pg.display.update()
					return
				if 0 < event.key - 48 < 10:
					pg.draw.rect(win, pg.Color("white"), (position[0]*50 + buffer, position[1]*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
					value = font.render(str(event.key-48), True, pg.Color("blue"))
					win.blit(value, (position[0]*50 + 15, position[1]*50))
					current[i-1][j-1] = event.key - 48
					pg.display.update()
					return
				return

def main():
	pg.init()
	win = pg.display.set_mode((WIDTH, WIDTH))
	pg.display.set_caption("Sudoku")
	win.fill(background_color)
	font = pg.font.SysFont("Papyrus", 35)

	for i in range(0,10):
		k = 4 if i%3 == 0 else 2
		pg.draw.line(win, pg.Color("black"), (50 + 50 * i, 50), (50 + 50 * i, 500), k)
		pg.draw.line(win, pg.Color("black"), (50, 50 + 50 * i), (500, 50 + 50 * i), k)

	pg.display.update()

	for i in range (0, len(board[0])):
		for j in range (0, len(board[0])):
			if(0 < board[i][j] < 10):
				value = font.render(str(board[i][j]), True, pg.Color("black"))
				win.blit(value, ((j+1) * 50 + 15, (i+1) * 50))

	pg.display.update()

	while True:
		for event in pg.event.get():
			if event.type == pg.MOUSEBUTTONUP and event.button == 1:
				pos = pg.mouse.get_pos()
				insert(win, (pos[0]//50, pos[1]//50))
			if event.type == pg.QUIT:
				pg.quit()
				return

main()