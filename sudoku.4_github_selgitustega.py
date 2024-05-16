import pygame as pg
import numpy as np
import random

WIDTH = 550
background_color = pg.Color("white")

# Algse laua, praeguse laua ja vastuse loomine
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

# Funktsioon, mis näitab hetkelise sudoku laua olekut
def PossibleValueAtPosition(pz:[], row:int, col:int):
    r=row//3*3 #arvutab 3x3 ruudu alguse
    c=col//3*3 
    return {1,2,3,4,5,6,7,8,9}.difference(set(pz[r:r+3,c:c+3].flat)).difference(set(pz[row,:])).difference(set(pz[:,col])) 
#tagastab võimalikud väärtused, mis on {1,2,3,4,5,6,7,8,9} sees, kuid mitte set1, set2 või set3 sees.

# Funktsioon, mis loendab lahenduste arvu antud laual
def Solution_Count(pz:[], n:int, Nof_solution:int):
    if Nof_solution>1: #kui on rohkem kui 1 lahendus, siis tagastab Nof_solution
        return Nof_solution
    if n>=81: #kui n on suurem või võrdne 81-ga, siis on laud täidetud
        Nof_solution+=1 #suurendab lahenduste arvu
        return Nof_solution
    (row,col) = divmod(n,9) 
    if pz[row][col]>0: #kui antud positsioonil on juba väärtus, siis liigub järgmisele positsioonile
        Nof_solution = Solution_Count(pz, n+1, Nof_solution) #  kasutab rekursiooni(kutsub ise end välja) ja liigume järgmisele positsioonile
    else:
        l = PossibleValueAtPosition(pz, row,col)
        for v in l: 
            pz[row][col] = v #paneb antud positsioonile väärtuse
            Nof_solution = Solution_Count(pz, n+1, Nof_solution) 
            pz[row][col] = 0 #kui ei leia lahendust, siis paneb antud positsioonile 0
    return Nof_solution	# tagastab lahenduste arvu

# Sudoku lahendaja funktsioon
def SudokuSolver(pz:[], n:int): # pz on laud, n on positsioon
    if n==81: # kui n on 81, siis on laud täidetud
        return True
    (row,col) = divmod(n,9) # arvutab rea ja veeru
    if pz[row][col]>0: # kui antud positsioonil on juba väärtus, siis liigub järgmisele positsioonile
        if SudokuSolver(pz, n+1): 
            return True # kui leiab lahenduse, siis tagastab True
    else: #kui (pz[row][col])) on tühi, siis 
        l = list(PossibleValueAtPosition(pz, row,col)) #
        random.shuffle(l) #segab listi
        for v in l:#võtab väärtuse listist
            pz[row][col] = v #paneb antud positsioonile väärtuse
            if SudokuSolver(pz, n+1): #kasutab rekursiooni(kutsub ise end välja) ja liigub järgmisele positsioonile
                return True
            pz[row][col] = 0 #kui ei leia lahendust, siis paneb antud positsioonile 0
    return False   

# Funktsioon, mis kaevab auke täielikult lahendatud lauale, et luua mõistatus
def DigHoles(pz:[], randomlist:[], n:int): #pz on laud, randomlist on list, kus on juhuslik järjend, n on positsioon
    global board #kasutab globaalset muutujat
    if n>=81: #kui n on suurem või võrdne 81-ga, siis tagastab
        return
    (row,col) = divmod(randomlist[n],9) #arvutab rea ja veeru
    if pz[row][col]>0: #kui antud positsioonil on juba väärtus, siis liigub järgmisele positsioonile
        pz_check=pz.copy() #teeb koopia lauast
        pz_check[row][col]=0  #võrdustab antud positsiooni 0-ga
        Nof_solution = Solution_Count(pz_check, 0, 0) #kontrollib lahenduste arvu
        if Nof_solution==1: #kui on 1 lahendus, siis paneb antud positsioonile 0
            pz[row][col]=0 #võrdustab antud positsiooni 0-ga
            board = pz #võrdustab laua pz-ga
    DigHoles(pz, randomlist, n+1) #eemaldab väärtused juhuslikult valitud lahtritest, jätkab, kuni kõik indeksid läbi käidud

# Funktsioon, mis genereerib uue laua
def generate_board():
    global answer #muudab kõiki järgnevaid muutujaid
    puzzle = np.zeros((9,9), dtype=int)  #teeb numpy'ga 9x9 maatriksi, kus kõik väärtused on 0
    SudokuSolver(puzzle, 0) #kasutab SudokuSolver funktsiooni, kus puzzle mõistatus ja 0, kust algab lahenduste otsimine
    for i in range (0, 9): #iga muutuja kohta i vahemikus 0 kuni 9
        for j in range (0, 9): #iga muutuja kohta j vahemikus 0 kuni 9
            answer[i][j] = puzzle[i][j] #määrab answer[i][j] väärtuseks puzzle[i][j] sama positsiooni elemendi väärtuse
    randomlist = list(range(81)) # teeb listi vahemikus 0 kuni 81
    random.shuffle(randomlist) #segab
    DigHoles(puzzle, randomlist, 0) #tühjad kohad alates randomlisti esimesest indeksist

# Funktsioon, mis lisab kasutaja sisestatud väärtuse lauale
def insert(win, position): # defineerib fn insert, argumendiks win ja position
    global current, board #kasutab globaalseid muutujaid
    i,j = position[1], position[0] #i on positioni rea väärtus, j on positioni veeru väärtus, vastavalt 1 ja 0
    buffer = 5 
    font = pg.font.SysFont("Comic Sans MS", 35)
    while True: 
        for event in pg.event.get(): #iga eventi kohta pygame'is
            if event.type == pg.QUIT: #kontrollib, kui kasutaja on sulgenud akna
                return
            if event.type == pg.KEYDOWN: #kontrollib, kui kasutaja on vajutanud klahvi
                if board[i-1][j-1] != 0: #kontrollib, kas antud positsioonil on juba väärtus, mis pole null, kui tõene, siis lõpetab
                    return
                if event.key == 48: 
                    current[i-1][j-1] = event.key - 48 #kas on 0
                    pg.draw.rect(win, pg.Color("white"), (position[0]*50 + buffer, position[1]*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                    pg.display.update()
                    return
                if 0 < event.key - 48 < 10: #kas on sisestatud väärtus vahemikus 1 kuni 9, joonistab väärtuse, uuendab lauda
                    pg.draw.rect(win, pg.Color("white"), (position[0]*50 + buffer, position[1]*50 + buffer, 50 - 2*buffer, 50 - 2*buffer))
                    value = font.render(str(event.key-48), True, pg.Color("blue"))
                    win.blit(value, (position[0]*50 + 15, position[1]*50))
                    current[i-1][j-1] = event.key - 48
                    pg.display.update()
                    return
                return
        if isWin() == True: #kui kasutaja on võitnud, siis kuvab vastava teate
            win.blit(font.render("Sa võitsid", True, pg.Color("blue")), (230, 5))
            pg.display.update()
            return

# Peamine funktsioon, mis käivitab mängu
def main():
    pg.init()
    win = pg.display.set_mode((WIDTH, WIDTH)) #akna suurus, pealkiri ja taustvärv, stiil ja font
    pg.display.set_caption("Sudoku")
    win.fill(background_color)
    font = pg.font.SysFont("Comic Sans MS", 35)

    for i in range(0,10): #iga muutuja kohta i vahemikus 0 kuni 9
        k = 2 if i%3 != 0 else 4 #k väärtus on 2 kui ei jagu 3'ga, muidu väärtus 4
        pg.draw.line(win, pg.Color("black"), (50 + 50*i, 50), (50 + 50*i,500), k)
        pg.draw.line(win, pg.Color("black"), (50 , 50 + 50*i), (500,50 + 50*i), k)
    pg.display.update() #uuendab akent vastavalt muudatustele(joonistab jooned)

    for i in range (0, len(board[0])):  #kontrollib, kas KÕIKIDE elementide väärtus on vahemikus 0 kuni 9 ja joonistab vastavalt lauale
        for j in range (0, len(board[0])):
            if(0 < board[i][j] < 10):
                value = font.render(str(board[i][j]), True, pg.Color("black"))
                win.blit(value, ((j+1) * 50 + 15, (i+1) * 50))

    pg.display.update() #uuendab akent vastavalt muudatustele

    while True: 
        for event in pg.event.get():  
            if event.type == pg.MOUSEBUTTONUP and event.button == 1:  #tuvastab hiire positsiooni ja kutsub välja insert funktsiooni
                pos = pg.mouse.get_pos()
                insert(win, (pos[0]//50, pos[1]//50))
            if event.type == pg.QUIT: #kui sündmuse liik on quit, siis lõpetab fn töö
                pg.quit()
                return

# Funktsioon, mis kontrollib, kas kasutaja on võitnud
def isWin() -> bool: #kontrollib, kas praegune laud on võrdne vastusega
    global current, answer
    for i in range (0, 9):
        for j in range (0, 9):
            if (current[i][j] != answer[i][j]): 
                return False #kui praegune laud ei ole võrdne vastusega, siis tagastab False
    return True #kui praegune laud on võrdne vastusega, siis tagastab True

# Genereerib laua ja alustab mängu
generate_board()
current = board.copy()
main()