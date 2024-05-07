import pygame as pg
import numpy as np
import random

WIDTH = 550
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

answer = [
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

def PossibleValueAtPosition(pz:[], row:int, col:int):
	r=row//3*3
	c=col//3*3
	return {1,2,3,4,5,6,7,8,9}.difference(set(pz[r:r+3,c:c+3].flat)).difference(set(pz[row,:])).difference(set(pz[:,col]))

def Solution_Count(pz:[], n:int, Nof_solution:int):
	if Nof_solution>1:
		return Nof_solution
	if n>=81:
		Nof_solution+=1
		return Nof_solution
	(row,col) = divmod(n,9)
	if pz[row][col]>0:
		Nof_solution = Solution_Count(pz, n+1, Nof_solution)
	else:
		l = PossibleValueAtPosition(pz, row,col)
		for v in l:
			pz[row][col] = v
			Nof_solution = Solution_Count(pz, n+1, Nof_solution)
			pz[row][col] = 0
	return Nof_solution	

def SudokuSolver(pz:[], n:int):
	if n==81:
		return True
	(row,col) = divmod(n,9)
	if pz[row][col]>0:
		if SudokuSolver(pz, n+1):
			return True
	else:
		l = list(PossibleValueAtPosition(pz, row,col))
		random.shuffle(l)
		for v in l:
			pz[row][col] = v
			if SudokuSolver(pz, n+1):
				return True
			pz[row][col] = 0
	return False

def DigHoles(pz:[], randomlist:[], n:int):
	global board
	if n>=81:
		return
	(row,col) = divmod(randomlist[n],9)
	if pz[row][col]>0:
		pz_check=pz.copy()
		pz_check[row][col]=0
		Nof_solution = Solution_Count(pz_check, 0, 0)
		if Nof_solution==1:
			pz[row][col]=0
			board = pz
	DigHoles(pz, randomlist, n+1)

def generate_board():
	global answer
	puzzle = np.zeros((9,9), dtype=int)
	SudokuSolver(puzzle, 0)
	answer = puzzle
	randomlist = list(range(81))
	random.shuffle(randomlist)
	DigHoles(puzzle, randomlist, 0)

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
	font = pg.font.SysFont("Comic Sans MS", 35)

	for i in range(0,10):
		k = 2 if i%3 != 0 else 4
		pg.draw.line(win, pg.Color("black"), (50 + 50*i, 50), (50 + 50*i,500), k)
		pg.draw.line(win, pg.Color("black"), (50 , 50 + 50*i), (500,50 + 50*i), k)
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


generate_board()
current = board.copy()
main()
