##
# A GameBoard class for a game of Tic Tac Toe, and a ScoreBoard class for Tic Tac Toe
# Student Name: Will Malisch
# Student ID: wmalisch
# Student Number: 250846447

# Define a class for GameBoard
class GameBoard:

    # Set up the constructor. This includes the board, status of all potential wins, draws, etc.
    def __init__(self):
        self._boardtable = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self._boolX = False
        self._boolO = False
        self._line = ""
        self._rowWinX = False
        self._rowWinO = False
        self._rowWin = False
        self._columnWinX = False
        self._columnWinO = False
        self._columnWin = False
        self._crossWinX = False
        self._crossWinO = False
        self._crossWin = False
        self._full = False
        self._playerXWins = False
        self._playerOWins = False


    # A method for printing the current game board
    def printCurrentBoard(self):
        print("%s | %s | %s" % (self._boardtable[0][0],self._boardtable[0][1],self._boardtable[0][2]))
        print("---------")
        print("%s | %s | %s" % (self._boardtable[1][0],self._boardtable[1][1],self._boardtable[1][2]))
        print("---------")
        print("%s | %s | %s" % (self._boardtable[2][0],self._boardtable[2][1],self._boardtable[2][2]))

    ## A method that clears the gameboard, and resets all the boolean variables for wins so the players can restart
    # @param self
    # @return all False boolean variables and cleared board
    def clear(self):
        self._boardtable = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self._full = False
        self._rowWin = False
        self._rowWinX = False
        self._rowWinO = False
        self._columnWinX = False
        self._columnWinO = False
        self._columnWin = False
        self._crossWinX = False
        self._crossWinO = False
        self._crossWin = False
        self._playerXWins = False
        self._playerOWins = False
        self._noWinners = False

    # A method to place an X tic
    # @param self, i is the row coordinate, j is the column coordinate
    # @return update board table and return True if move legal
    def placeX(self,i,j):
        i = int(i)
        j = int(j)

        # Test that there isn't a tic already in the location
        if self._boardtable[i-1][j-1] == " ":
            self._boolX = True
        else:
            self._boolX = False

        # Only update the location if the above is proved to be true
        if self._boolX == True:
            self._boardtable[i-1][j-1] = "X"
        return self._boolX


    ## A method for placing an O tic
    # @param self, i is the row coordinate, j is the column coordinate
    # @return update board table and return True if move legal
    def placeO(self,i,j):
        i = int(i)
        j = int(j)

        # Test that there isn't a tic already in the location
        if self._boardtable[i-1][j-1] == " ":
            self._boolO = True
        else:
            self._boolO = False

        # Only update the location if the above is proved to be true
        if self._boolO == True:
            self._boardtable[i-1][j-1] = "O"
        return self._boolO

    # A method for deciding a winner
    # @param self
    # @return True if there is a winner, determined if the functions below are satisfied as True
    def decideWinner(self):
        self.crossWinner()
        self.rowWinner()
        self.columnWinner()
        if self._crossWin == True:
            if self._crossWinX == True:
                self._playerXWins = True
                return self._playerXWins
            elif self._crossWinO == True:
                self._playerOWins = True
                return self._playerOWins
        elif self._rowWin == True:
            if self._rowWinX == True:
                self._playerXWins = True
                return self._playerXWins
            elif self._rowWinO == True:
                self._playerOWins = True
                return self._playerOWins
        elif self._columnWin == True:
            if self._columnWinX == True:
                self._playerXWins  = True
                return self._playerXWins
            elif self._columnWinO == True:
                self._playerOWins = True
                return self._playerOWins
        else:
            return False

    ## A function to check if a player has won a row, and check if it was an X or O
    # @param self
    # @return True if there is a row with XXX or OOO
    def rowWinner(self):
        for i in range(3):
            for j in range(3):
                self._line = self._line + str(self._boardtable[i][j])
            if self._line in "XXX":
                self._rowWinX = True
                self._rowWin = True
                break
            elif self._line in "OOO":
                self._rowWin = True
                self._rowWinO = True
                break
            self._line = ""
        return self._rowWin

    ## A function to check if a player has won a column, and check if it was an X or O
    # @param self
    # @return True if there is a column with XXX or OOO
    def columnWinner(self):
        for i in range(3):
            for j in range(3):
                self._line = self._line + str(self._boardtable[j][i])
            if self._line in "XXX":
                self._columnWinX = True
                self._columnWin = True
                break
            elif self._line in "OOO":
                self._columnWin = True
                self._columnWinO = True
                break
            self._line = ""
        return self._columnWin

    ## A function to check if a player has won a diagonal line, and check if it was an X or O
    # @param self
    # @return True if there is a column with XXX or OOO
    def crossWinner(self):
        if (self._boardtable[0][0] + self._boardtable[1][1] + self._boardtable[2][2]) in "XXX" or (self._boardtable[0][2] + self._boardtable[1][1] + self._boardtable[2][0]) in "XXX":
            self._crossWinX = True
            self._crossWin = True
        elif (self._boardtable[0][0] + self._boardtable[1][1] + self._boardtable[2][2]) in "OOO" or (self._boardtable[0][2] + self._boardtable[1][1] + self._boardtable[2][0]) in "OOO":
            self._crossWinO = True
            self._crossWin = True
        return self._crossWin

    ## A function to test if the board is full
    # @param self
    # @return True if there are only X's and O's on the board
    def boardFull(self):
        for i in range(3):
            for j in range(3):
                self._line = self._line + self._boardtable[i][j]
        if (" " in self._line) == False:
            self._full = True
            return self._full
        return self._full

# Define a class for ScoreBoard
class ScoreBoard:

    # Set up constructor
    def __init__(self,lst):
        self._results = [[0,0,0],[0,0,0]]
        self._lst = lst

    ## A method to print the scoreboard
    # @param self
    # @return a updated and printed scoreboard for all the players who have played
    def printScoreBoard(self):
        print("               Name | Wins | Losses | Draws ")
        print("--------------------|------|--------|-------")
        for i in range(0,len(self._lst)):
            print("%-20s|    %s |     %s  |     %s " % (self._lst[i],self._results[i][0],self._results[i][1],self._results[i][2]))

    ## A method to add a win to a players score track
    # @param self, and the players name who gets the win
    # @return an updated scoreboard
    def addWin(self, name):
        for i in range(0,len(self._lst)):
            if name in self._lst[i]:
                self._results[i][0] = self._results[i][0] + 1
            elif len(self._results) < len(self._lst):
                self._results.append([0,0,0])

    ## A method to add a loss to a players score track
    # @param self, and the players name who gets the loss
    # @return an updated scoreboard
    def addLoss(self, name):
        for i in range(0,len(self._lst)):
            if name in self._lst[i]:
                self._results[i][1] = self._results[i][1] + 1
            elif len(self._results) < len(self._lst):
                self._results.append([0,0,0])

    ## A method to add a draw to a players score track
    # @param self, and the players name who gets the draw
    # @return an updated scoreboard
    def addDraw(self, name):
        for i in range(0,len(self._lst)):
            if name in self._lst[i]:
                self._results[i][2] = self._results[i][2] + 1
            elif len(self._results) < len(self._lst):
                self._results.append([0,0,0])


game = GameBoard()
game.placeX(1,1)
game.placeX(2,2)
game.placeX(3,3)
print(game.rowWinner())
