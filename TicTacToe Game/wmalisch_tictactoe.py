

from myBoards import GameBoard
from myBoards import ScoreBoard

## Define mmain function
# @param/return no paramter or return, just run the instructions inside the function
def main():
    # Initialize the gameboard
    game = GameBoard()

    ## Validates that the users input for tic coordinates is legal
    # @param lst is the users input parsed into a list
    # @return True if the list was valid based on checkNumeric, checkXY, checkLength, and checkCurrentBoardSpace
    def checkInput(lst):
        validInput = False
        if checkLength(lst) == True and checkNumeric(lst) == True and checkXY(lst) == True and checkCurrentBoardSpace(lst) == True:
                validInput = True
        return validInput

    ## Validates that there are only 2 values in the users input
    # @param lst is the users input parsed into a list
    # @returnTrue if the list is 2 values long, False if it is not
    def checkLength(lst):
        validLength = False
        if len(lst) == 2:
            validLength = True
            return validLength
        else:
            print("Your input has either to many or to few characters. Adjust so it has only 2.")
        return validLength

    ## Validates that there are only numeric values in the user input
    # @param lst is the users input parsed into a list
    # @returnTrue if the values are only numeric, False if it is not
    def checkNumeric(lst):
        validNumeric = False
        if lst[0].isnumeric() == lst[1].isnumeric() == True:
            validNumeric = True
            return validNumeric
        if validNumeric == False:
            print("You're not allowed alpha characters in your input.")
        return validNumeric

    ## Validates that the user input will be on the board
    # @param lst is the users input parsed into a list
    # @returnTrue if the input is either a 1, 2 or 3 (on the board), False if it is not
    def checkXY(lst):
        validXY = False
        if (lst[0] == "1" or lst[0] == "2" or lst[0] == "3") and (lst[1] == "1" or lst[1] == "2" or lst[1] == "3"):
            validXY = True
            return validXY
        else:
            print("The inputs must be either a 1, 2 or 3.")
        return validXY

    ## Validates that there isn't currently a tic in the inputted location
    # @param lst is the users input parsed into a list
    # @returnTrue if there is no tic in the inputted location, False if it is not
    def checkCurrentBoardSpace(lst):
        validCurrentBoardSpace = False
        if game._boardtable[int(lst[0])-1][int(lst[1])-1] == " ":
            validCurrentBoardSpace = True
            return validCurrentBoardSpace
        else:
            print("You can not place a marker in a spot that is already taken.")
        return validCurrentBoardSpace

    # Print the instructions
    print("We are playing tic tac toe!")
    print("To play the game enter two numbers to indicate where to place\neach game piece. Enter numbers from 1 to 3.\n(1 1) is the top left corner. (3 3) is the bottom right corner.")

    # Initialize the list of players and the scoreboard with those players before the loop, so it is not overwritten
    players = []
    score = ScoreBoard(players)

    # Loop behind gameplay that records scores, reset variables, and asks if they want to play again
    replay = "y"
    while replay.lower() == "y":
        game.clear()
        # Take player names for X and O
        player1 = input("Who will be playing as X? ")
        player2 = input("Who will be playing as O? ")

        # Add the player to the scoreboard if they have not already played
        if player1 not in players:
            players.append(player1)
        if player2 not in players:
            players.append(player2)

        # Run the loop that asks for X and O positions until someone wins or the board is full
        runLoop = True
        while runLoop:
            # Take player1's move
            game.printCurrentBoard()
            print("%s's turn!" % player1,end="")
            move = input(" Where should X go? ")

            # Convert player1's input into numbers processable for the gameboard class
            move = move.split()
            validTic = checkInput(move)

            # Test if the input is valid using functions above. If it is invalid, prompt them until it is valid
            while validTic == False:
                move = input("Where should X go? ")
                move = move.split()
                validTic = checkInput(move)

            # Place the X on the board, and print the board
            game.placeX(int(move[0]),int(move[1]))
            # End gameplay loop if there is a winner or a draw. Update and print the scores for the players
            if game.decideWinner() == True:
                print("Winner is X!")
                game.printCurrentBoard()
                score.addWin(player1)
                score.addLoss(player2)
                score.printScoreBoard()
                break
            elif game.boardFull() == True:
                print("Board is full. Match is a draw.")
                game.printCurrentBoard()
                score.addDraw(player1)
                score.addDraw(player2)
                score.printScoreBoard()
                break

            # Take player1's move
            game.printCurrentBoard()
            print("%s's turn!" % player2,end="")
            move = input(" Where should O go? ")

            # Convert player1's input into numbers processable for the gameboard class
            move = move.split()
            validTic = checkInput(move)

            # Test if the input is valid using functions above. If it is invalid, prompt them until it is valid
            while validTic == False:
                move = input("Where should O go? ")
                move = move.split()
                validTic = checkInput(move)

            # Place the X on the board, annd prinbt the board
            game.placeO(int(move[0]),int(move[1]))

            # End gameplay loop if there is a winner or a draw. Update and print the scores for the players
            if game.decideWinner() == True:
                print("Winner is O!")
                game.printCurrentBoard()
                score.addWin(player2)
                score.addLoss(player1)
                score.printScoreBoard()
                break
            elif game.boardFull() == True:
                print("Board is full. Match is a draw.")
                game.printCurrentBoard()
                score.addDraw(player1)
                score.addDraw(player2)
                score.printScoreBoard()
                break

        # Prompt the user to play again, and start back at the gameplay loop
        replay = input("Do you want to play again? (Y/N) ")

# Run the program
main()

