# A 2048 game implementation 

import random as rnd
import os
import sys

class Grid():
    def __init__(self, row=4, col=4, initial=2):
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
        # take a cell number and return
        # the row and column index for that number
        row = cell//self.col
        col = cell%self.col
        return row, col
    
    def getCellNumber(self, row, col):
        # algorithm to get cell_number for a given index
        # (row * length of column) + column number        
        cell_number = (row*self.col) + col  
        return cell_number          
    
    def setCell(self, cell, val):
        # set new value of cell
        row, i = self.getCellId(cell)   # get cell index first     
        self._grid[row][i] = val
                       

    def getCell(self, cell):
        # return value of given cell
        row, i = self.getCellId(cell)   # get cell index first
        return self._grid[row][i]
              
    
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
                self.setCell(cell, 2)
            else:
                cdf = rnd.random()
                if cdf > 0.75:
                    self.setCell(cell, 4)
                else:
                    self.setCell(cell, 2)
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
                    line += ' '.center(5) + '|'
                else:
                    line += str(self.getCell((i * self.row) + j)).center(5) + '|'
            print(line)
        print()
        
    
    def updateEmptiesSet(self):
        """
        This function should update the list of empty cells of the grid.
        """
        self.emptiesSet = []  
        for cell in range(self.row*self.col):
            # iterate through every cell and check for 0            
            if self.getCell(cell) == 0:
                self.emptiesSet.append(cell)
       
    
    def collapsible(self): 
        # check if grid can collapse
        collapse = False
        # iterate throgh every cell
        for row in range(self.row):
            for i in range(self.col):
                if self.getCell(self.getCellNumber(row,i)) == 0:    # check for empty cell
                    collapse = True
                    
                elif i < self.col-1 and self.getCell(self.getCellNumber(row,i)) == self.getCell(self.getCellNumber(row,i+1)):   # check horizontal match
                    collapse = True
                    
                elif row < self.row-1 and self.getCell(self.getCellNumber(row,i)) == self.getCell(self.getCellNumber(row+1,i)):  # check vertical match 
                    collapse = True
                
        return collapse

    def collapseRow(self, lst):
        # collapse cells in list toward left
        # return if row collapsed
        collapse = False
        for cell in range(len(lst)-1):
            i = cell + 1
            while i<len(lst)-1 and lst[i] == 0:  # skip over 0s
                i += 1
            if lst[cell] == lst[i] and lst[cell] != 0:  # check match
                lst[cell] = lst[cell]*2     # merge numbers
                self.score += lst[cell] 
                lst[i] = 0  # delete right cell that was merged
                collapse = True
        for cell in range(len(lst)-1):
            # get rid of empty spaces b/w cells
            if lst[cell] == 0:
                i = cell + 1
                while lst[i] == 0 and i<len(lst)-1: # skip over 0
                    i += 1
                if lst[i] != 0:
                    collapse = True
                lst[cell] = lst[i]  # collapse cell to left
                lst[i] = 0  # empty original cell index
        return lst, collapse


    def collapseLeft(self):
        # collapse all rows to left
        collapse = False
        for row in range(self.row):
            lst = []            
            for col in range(self.col):
                lst.append(self.getCell(self.getCellNumber(row, col)))
            lst, fall = self.collapseRow(lst)
            if fall:
                collapse = True # set true even when a single row is true
                i = 0
                for cell in lst:
                    self.setCell(self.getCellNumber(row, i), cell)
                    i += 1
        return collapse


    def collapseRight(self):
        # collapse all rows to right        
        collapse = False
        for row in range(self.row):
            lst = []
            for col in range(self.col):
                lst.append(self.getCell(self.getCellNumber(row, col)))
            # reverse list so it collapses left
            lst.reverse()
            lst, fall = self.collapseRow(lst)
            # reverse back list so final result is collapse right
            lst.reverse()
            if fall:
                collapse = True
                i = 0
                for cell in lst:
                    self.setCell(self.getCellNumber(row, i), cell)
                    i += 1                
        return collapse 
    
        
    def collapseUp(self):
        # collapse all columns up
        collapse = False
        for col in range(self.col):
            lst = []            
            for row in range(self.row):
                lst.append(self.getCell(self.getCellNumber(row, col)))   # get list of cells in column
            lst, fall = self.collapseRow(lst)
            if fall:
                collapse = True
                for row in range(self.row):  # iterate nth position through every row
                    self.setCell(self.getCellNumber(row, col), lst[row])
        return collapse
    


    def collapseDown(self):
        # collapse all columns down
        collapse = False
        for col in range(self.col):
            lst = []            
            for row in range(self.row):
                lst.append(self.getCell(self.getCellNumber(row, col)))    # list of cells in a certain column
            lst.reverse()   # reverse to collapse up
            lst, fall = self.collapseRow(lst)
            lst.reverse()   # reverse to finally collapse down            
            if fall:
                collapse = True
                for row in range(self.row):
                    self.setCell(self.getCellNumber(row, col), lst[row])
                     # assign cell from list to column
        return collapse



class Game():
    def __init__(self, row=4, col=4, initial=2):
    
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
                    self.game.updateEmptiesSet()
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
    pass
main()
