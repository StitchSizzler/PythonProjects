'''
This is the game of tic-tac-toe. 
On the left will be a tic-tac-toe game grid
and on the rigt will be a legend grid. 
Players can indicate the key on the
legend grid that corresponds to the game grid
on the left, in order to make their mark. 
'''
def main():
    myBoard = TicTacToe()
    continueGame = True
    playerX = True  # check who's turn it is
    myBoard.drawBoard()
    
    while continueGame:
        if not myBoard.boardFull():
            # switch player symbol
            if playerX:
                ch = "x"
            else:
                ch = "o"
            validMove = False
            # continue the turn until player enters a valid move
            while validMove == False:
                move = input("It is the turn for " + ch + ". What is your move?")
                try:
                    move = int(move)
                    # check domain of the move (1-9)
                    if move<=9 and move>=1:
                        if myBoard.cellIsEmpty(move):
                            myBoard.assignMove(move, ch)
                            # swith player turns if move successful 
                            if playerX:
                                playerX = False 
                            else:
                                playerX = True
                            validMove = True    # can break out of loop and switch turns
                            print("\n")                                  
                            myBoard.drawBoard()
                            # check for a winner
                            winner = myBoard.whoWon()
                            if myBoard.whoWon() != "":
                                print(winner, "wins. Congrats!")
                                continueGame = False
                                break
                    else:
                        print("Input not valid. Choose an empty cell between 1-9")
                except:
                    "Input not valid."
        else:
            print("It's a tie.")
            continueGame = False
 
class TicTacToe:
    def __init__(self):
        # "board" is a list of 10 strings representing the board (ignore index 0)
        self.board = [" "]*10
        self.board[0]="#"

#------------------------------------------------------------- 
    def drawBoard(self):
    # This method prints out the board with current plays adjacent to a board with index.
        i=9
        while i>0:
            print(" %s | %s | %s      %d | %d | %d " % (self.board[i-2], self.board[i-1], self.board[i], i-2, i-1, i))
            i -= 3
            if i>=3:
                print("-----------    -----------")       
                
#------------------------------------------------------------- 
    def boardFull(self):
    # This method checks if the board is already full and returns True. Returns false otherwise
        isFull = False
        if " " not in self.board:
            isFull = True
        return isFull

#------------------------------------------------------------- 
    def cellIsEmpty(self, cell):
        isEmpty = False
        #try:
        if self.board[cell] == " ":
            isEmpty = True
    #except:
        #pass
        return isEmpty

#------------------------------------------------------------- 
    def assignMove(self, cell,ch):
    # assigns the cell of the board to the character ch      
        self.board[cell] = ch

#------------------------------------------------------------- 
    def whoWon(self):
    # returns the symbol of the player who won if there is a winner, otherwise it returns an empty string. 
        if self.isWinner("x"):
            return "x"
        elif self.isWinner("o"):
            return "o"
        else:
            return ""

#-------------------------------------------------------------   
    def isWinner(self, ch):
    # Given a player's letter, this method returns True if that player has won.
        win = False
        # check horizontal win
        i=9
        while i>0:
            if ch==self.board[i-2]==self.board[i-1]==self.board[i]:
                win = True
                return win
            else:
                i -= 3
        # check vertical win
        i=9
        while i>6:
            if ch==self.board[i]==self.board[i-3]==self.board[i-6]:
                win = True
                return win
            else:
                i-=1
        # check diagonal win:
        i=9
        if ch==self.board[i]==self.board[i-4]==self.board[i-8]:
            win = True
            return win
        elif ch==self.board[i-2]==self.board[i-4]==self.board[i-6]:
            win = True
            return win
        else:
            return win



main()