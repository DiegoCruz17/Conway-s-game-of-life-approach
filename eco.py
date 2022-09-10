from cell import Cell
import random
#The ecosystem class populates an array with cell objects and contains methods for handling the state of the cells.
class Ecosystem:
    def __init__(self,boardsize,win_size):
        self.boardsize = boardsize
        self.win_size = win_size
        self.cells = [[[]for x in range(0,self.boardsize)]for y in range(0,self.boardsize)]
        self.setting = True
        for row in range(0,self.boardsize):
            for col in range(0,self.boardsize):
                if random.randint(1,3) == 1:
                    self.cells[row][col] = Cell(col,row,self.win_size/self.boardsize,True)
                else:
                    self.cells[row][col] = Cell(col,row,self.win_size/self.boardsize)

    def updateEco(self,screen):
        for row in self.cells:
            for cell in row:
                cell.draw(screen)
                if not self.setting:
                    self.defineCellState(cell.x,cell.y)
    #this block surely needs optimization. It does not follow DRY either.
    def checkCell(self,x,y):
        alivecells = 0
        if x == 0 and y == 0:
            if self.cells[y][x+1].alive:
                alivecells +=1
            if self.cells[y+1][x].alive:
                alivecells +=1
            if self.cells[y+1][x+1].alive:
                alivecells +=1
            return alivecells
        elif x == self.boardsize - 1 and y == 0:
            if self.cells[y][x-1].alive:
                alivecells +=1
            if self.cells[y+1][x-1].alive:
                alivecells +=1
            if self.cells[y+1][x].alive:
                alivecells +=1
            return alivecells
        elif x == 0 and y == self.boardsize - 1:
            if self.cells[y-1][x].alive:
                alivecells +=1
            if self.cells[y-1][x+1].alive:
                alivecells +=1
            if self.cells[y][x+1].alive:
                alivecells +=1 
            return alivecells
        elif x == self.boardsize - 1 and y == self.boardsize - 1:
            if self.cells[y-1][x-1].alive:
                alivecells +=1
            if self.cells[y-1][x].alive:
                alivecells +=1
            if self.cells[y][x-1].alive:
                alivecells +=1
            return alivecells
        elif x == 0 and (y != 0 or y != self.boardsize - 1):            
            if self.cells[y-1][x].alive:
                alivecells +=1
            if self.cells[y-1][x+1].alive:
                alivecells +=1
            if self.cells[y][x+1].alive:
                alivecells +=1
            if self.cells[y+1][x].alive:
                alivecells +=1
            if self.cells[y+1][x+1].alive:
                alivecells +=1
            return alivecells
        elif x == self.boardsize - 1 and (y != 0 or y != self.boardsize - 1):            
            if self.cells[y-1][x].alive:
                alivecells +=1
            if self.cells[y-1][x-1].alive:
                alivecells +=1
            if self.cells[y][x-1].alive:
                alivecells +=1
            if self.cells[y+1][x].alive:
                alivecells +=1
            if self.cells[y+1][x-1].alive:
                alivecells +=1
            return alivecells
        elif y == 0 and (x != 0 or x != self.boardsize - 1):            
            if self.cells[y][x -1].alive:
                alivecells +=1
            if self.cells[y][x+1].alive:
                alivecells +=1
            if self.cells[y+1][x+1].alive:
                alivecells +=1
            if self.cells[y+1][x].alive:
                alivecells +=1
            if self.cells[y+1][x-1].alive:
                alivecells +=1
            return alivecells
        elif y == self.boardsize - 1 and (x != 0 or x != self.boardsize - 1):            
            if self.cells[y][x -1].alive:
                alivecells +=1
            if self.cells[y][x+1].alive:
                alivecells +=1
            if self.cells[y-1][x+1].alive:
                alivecells +=1
            if self.cells[y-1][x].alive:
                alivecells +=1
            if self.cells[y-1][x-1].alive:
                alivecells +=1
            return alivecells
        else:
            if self.cells[y][x-1].alive:
                alivecells +=1
            if self.cells[y][x+1].alive:
                alivecells +=1
            if self.cells[y-1][x+1].alive:
                alivecells +=1
            if self.cells[y-1][x].alive:
                alivecells +=1
            if self.cells[y-1][x-1].alive:
                alivecells +=1
            if self.cells[y+1][x-1].alive:
                alivecells +=1
            if self.cells[y+1][x+1].alive:
                alivecells +=1
            if self.cells[y+1][x].alive:
                alivecells +=1
            return alivecells

        
        
    def resetCells(self):
        for row in range(0,self.boardsize):
            for col in range(0,self.boardsize):
                self.cells[row][col] = Cell(col,row,self.win_size/self.boardsize)
    def defineCellState(self,x,y):
        alivecells = self.checkCell(x,y)
        if self.cells[y][x].alive:
            if alivecells <=3 and alivecells >= 2:
                self.cells[y][x].alive = True
            else:
                self.cells[y][x].alive = False
        else:
            if alivecells == 3:
                self.cells[y][x].alive = True


    
