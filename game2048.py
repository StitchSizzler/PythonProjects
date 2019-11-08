import random as rnd
import os
import sys

class Grid():
    def __init__(self, row=5, col=5, initial=2):
        self.row = row                              # number of rows in grid
        self.col = col                              # number of columns in grid
        self.initial = initial                      # number of initial cells filled
        self.score = 0
        
        self._grid = self.createGrid(row, col)    # creates the grid specified above

        self.emptiesSet = list(range(row * col))    # list of empty cells
                 
        for _ in range(self.initial):               # assignation to two random cells
            self.assignRandCell(init=True)


    def createGrid(self, row, col):
        
        grid = []
        for i in range(row):
            in_grid = []            
            for j in range(col):
                in_grid.append(0)   # add 0 to each column of row
            grid.append(in_grid)
        return(grid)

    def getCellId(self, cell):
        cell_id = -1
        for row in self._grid:
            for i in range(len(row)):
                cell_id += 1 # set index of cell                
                if cell_id == cell:
                    return row, i         
    
    def setCell(self, cell, val):
        row, i = self.getCellId(cell)        
        row[i] = val
                       

    def getCell(self, cell):
        row, i = self.getCellId(cell)
        return row[i]
              
    
    def assignRandCell(self, init=False):
    
        """
        This function assigns a random empty cell of the grid 
        a value of 2 or 4.
        
        In __init__() it only assigns cells the value of 2.
        
        The distribution is set so that 75% of the time the random cell is
        assigned a value of 2 and 25% of the time a random cell is assigned 
        a value of 4
        """
        if len(self.emptiesSet):
            cell = rnd.sample(self.emptiesSet, 1)[0]
            if init:
                self.setCell(cell, 5)
            else:
                cdf = rnd.random()
                if cdf > 0.75:
                    self.setCell(cell, 10)
                else:
                    self.setCell(cell, 5)
            self.emptiesSet.remove(cell)

            

    def drawGrid(self):
        pass
        """
        This function draws the grid representing the state of the game
        grid
        """
        
        for i in range(self.row):
            line = '\t|'
            for j in range(self.col):
                if not self.getCell((i * self.row) + j):
                    line += ' '.center(6) + '|'
                else:
                    line += str(self.getCell((i * self.row) + j)).center(6) + '|'
            print(line)
        print()
        
    
    def updateEmptiesSet(self):
    
        """
        This function should update the list of empty cells of the grid.
        """
        self.emptiesSet = []
        for row in range(len(self._grid)):
            for col in range(len(self._grid[0])):
                if self._grid[row][col] == 0:
                    cell_id = (row*len(self._grid[0])) + col 
                    self.emptiesSet.append(cell_id)      
    
    
    def collapsible(self):   
        empty = False
        for row in range(len(self._grid)):
            for i in range(len(self._grid[0])):
                if self._grid[row][i] == 0:
                    empty = True    # check for empty cell
                    
                elif i < len(self._grid[0])-1 and self._grid[row][i] == self._grid[row][i+1]:   # check horizontal match
                    empty = True
                    
                elif row < len(self._grid)-1 and self._grid[row][i] == self._grid[row+1][i]:  # check vertical match 
                    empty = True
                
        return empty

    def collapseRow(self, lst):
        new_lst = []
        collapse = False
        for cell in range(len(lst)-1):
            i = cell + 1
            while i<len(lst)-1 and lst[i] == 0:  # skip over 0s
                i += 1
            if lst[cell] == lst[i] and lst[cell] != 0: # check match
                lst[cell] = lst[cell]*2
                self.score += lst[cell]
                lst[i] = 0
                collapse = True
        for cell in range(len(lst)-1):
            if lst[cell] == 0:
                i = cell + 1
                while lst[i] == 0 and i<len(lst)-1:
                    i += 1
                if lst[i] != 0:
                    collapse = True
                lst[cell] = lst[i]
                lst[i] = 0
        return lst, collapse


    def collapseLeft(self):
        for row in self._grid:
            lst, collapse = self.collapseRow(row)
        self.updateEmptiesSet()
        return collapse


    def collapseRight(self):
        for row in self._grid:
            row.reverse()
            lst, collapse = self.collapseRow(row)
            row = lst.reverse()
        self.updateEmptiesSet()        
        return collapse 
    
        
    def collapseUp(self):
        collapse = False
        for col in range(len(self._grid[0])):
            lst = []            
            for row in self._grid:
                lst.append(row[col])
            lst, fall = self.collapseRow(lst)
            if fall:
                collapse = True
            for row in range(len(self._grid)):
                self._grid[row][col] = lst[row]
        self.updateEmptiesSet()
        return collapse
    


    def collapseDown(self):
        collapse = False
        for col in range(len(self._grid[0])):
            lst = []            
            for row in self._grid:
                lst.append(row[col])
            lst.reverse()
            lst, fall = self.collapseRow(lst)
            if fall:
                collapse = True
            lst.reverse()
            for row in range(len(self._grid)):
                self._grid[row][col] = lst[row]
        self.updateEmptiesSet()
        return collapse



class Game():
    def __init__(self, row=5, col=5, initial=2):
    
        """
        Creates a game grid and begins the game
        """
        
        self.game = Grid(row, col, initial)
        self.play()
    
    
    def printPrompt(self):
        
        """
        Prints the instructions and the game grid with a move prompt
        """
    
        if sys.platform == 'win32':
            os.system("cls")
        else:
            os.system("clear")
        
        print('Press "w", "a", "s", or "d" to move Up, Left, Down or Right respectively.')
        print('Enter "p" to quit.\n')
        self.game.drawGrid()
        print('\nScore: ' + str(self.game.score))


    def play(self):
    
        moves = {'w' : 'Up',
                 'a' : 'Left',
                 's' : 'Down',
                 'd' : 'Right'}
        
        stop = False
        collapsible = True
        
        while not stop and collapsible:
            self.printPrompt()
            key = input('\nEnter a move: ')
            
            while not key in list(moves.keys()) + ['p']:
                self.printPrompt()
                key = input('\nEnter a move: ')

            if key == 'p':
                stop = True
            else:
                move = getattr(self.game, 'collapse' + moves[key])
                collapsed = move()
                
                if collapsed:
                    self.game.assignRandCell()
                    
                collapsible = self.game.collapsible()
                 
        if not collapsible:
            if sys.platform == 'win32':
                os.system("cls")
            else:
                os.system("clear")
            print()
            self.game.drawGrid()
            print('\nScore: ' + str(self.game.score))
            print('No more legal moves.')
            

def main():
    game = Game()
    
main()
