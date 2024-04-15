import pygame as pg
import numpy as np
import random

WIDTH = 645
background_color = pg.Color("white")

board = [
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9],
	[1,2,3,4,5,6,7,8,9]
]


def main():
	pg.init()
	win = pg.display.set_mode((WIDTH, WIDTH))
	pg.display.set_caption("Sudoku")
	win.fill(background_color)
	font = pg.font.SysFont("Carlito", 35)

	for i in range(0,10):
		k = 2 if i%3 != 0 else 4 
		pg.draw.line(win, pg.Color("black"), (60 + 60*i, 60), (60 + 60*i,600), k) 
		pg.draw.line(win, pg.Color("black"), (60 , 60 + 60*i), (600,60 + 60*i), k)

	pg.display.update()

	for i in range (0, len(board[0])):
		for j in range (0, len(board[0])):
			if(0 < board[i][j] < 10):
				value = font.render(str(board[i][j]), True, pg.Color("black"))
				win.blit(value, ((j+1) * 60 + 20, (i+1) * 60)) 

	pg.display.update()

	while True:
		for event in pg.event.get():
			if event.type == pg.MOUSEBUTTONUP and event.button == 1:
				pos = pg.mouse.get_pos()
				
			if event.type == pg.QUIT:
				pg.quit()
				return


main()
