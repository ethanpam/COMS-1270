# Ethan Pham           10/25/25      COMS-1270 Section 4
# Assignment 4 - Four in Sequence
# This is a game

# CITATION: Much of the code in this assignment is heavily modified/ adapted from code originally created by ChatGPT
# CITATION: ACCESSED: 3-15-2023
# CITATION: URL: https://chat.openai.com

import random
import sys


def printTitleMaterial():
    print("Four in Sequence!\nModified by Ethan Pham\nCOMS-1270 Section 4 ")


def initialChoice():
    """Allows the user to choose whether to [p]lay, get [i]nstructions, or [q]uit.

    :return string: choice - A string containing either 'p', 'i', or 'q'.
    """
    choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    while choice not in ("p", "i", "q"):
        print("ERROR: Please enter 'p', 'i', or 'q'...")
        choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    return choice


def chooseNumPlayers():
    """Allows the user to choose whether to play a game with [1] or [2] players.

    :return int: numPlayers - An integer, limited to strictly 1 or 2, to indicate the number of players in the game.
    """
    numPlayers = int(input("Number of Players? [1] / [2]: "))
    while numPlayers not in (1, 2):
        print("ERROR: Please enter either 1 or 2...")
        numPlayers = int(input("Number of Players? [1] / [2]: "))
    return numPlayers


def printBanner():
    """Prints out a nice header to delineate the game from the previous text output."""
    print("#######################################################################")
    print()
    print("~~ Starting New Round ~~")
    print()


def getPlayerPiece(playerNumber):
    """Returns a string corresponding to the 'player' under consideration. Player 0 corresponds to an 'empty' square.
    Player 1 corresponds to the 'X' pieces. Player 2 corresponds to the 'O' pieces.

    :param int playerNumber: The 'player' whose piece we wish to know.
    :return string: piece - A string containing either '.', 'X', or 'O' for player 0 (empty), 1, or 2, respectively.
    """
    if playerNumber == 0:
        return "."
    elif playerNumber == 1:
        return "X"
    elif playerNumber == 2:
        return "O"
    return "."


def createBoard(width, height):
    """Creates the underlying data structure for the game - a list of lists. This function also sets all the 'spaces'
    in the 'gameboard' to be 'empty' (player 0) spaces.

    :param int width: How many 'spaces' wide to make the gameboard.
    :param int height: How many 'spaces' high to make the gameboard.
    :return list of lists: board - The data structure that contains the contents of the gameboard. Only contains 'Player 0' pieces by default.
    """
    empty = getPlayerPiece(0)
    board = []
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(empty)
        board.append(row)
    return board


def printBoard(board):
    """Prints out the gameboard to the screen - including a row of digits at the bottom which correspond to columns the players can choose.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    """
    for row in board:
        for column in row:
            print(column, end="")
        print()
    for i in range(0, len(board[0])):
        print(i, end="")
    print()
    print()


def getColumnInt(board, playerNumber):
    """Take in user input as a string, and convert it to an integer. This function constructs a prompt based on the
    playerNumber, and the number of columns on the gameboard.

    NOTE: This function does not apply any filtering or input validation of any kind - it just gets the number from the user.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int playerNumber: The player number to display on the text output.
    :return int: The number that the user entered.
    """
    return int(input("Player {0}, please select a column between (0-{1}): ".format(playerNumber, len(board[0]) - 1)))


def getInputInRange(board, playerNumber):
    """Prompt the user to enter an integer between 0 and the number of columns on the board minus one.
    This function will enforce this range, and will not allow values outside of it.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int playerNumber: The player number to display on the text output.
    :return int: col - The column the player wants to drop a piece inside.
    """
    col = getColumnInt(board, playerNumber)
    while col < 0 or col > len(board[0]) - 1:
        print("ERROR: Value must be between (0-{0}). You entered: {1}".format(len(board[0]) - 1, col))
        col = getColumnInt(board, playerNumber)
    return col


def getHumanInput(board, playerNumber):
    """Collects input from a player for the column they want to drop a piece into.
    Ensures column is valid and not full.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int playerNumber: The player number to display on the text output.
    :return int: col - The column the player wants to drop a piece inside.
    """
    col = getInputInRange(board, playerNumber)
    while getOpenRow(board, col) == -1:
        print("ERROR: Column {0} is full! Please choose a different column...".format(col))
        col = getInputInRange(board, playerNumber)
    return col


def checkForNextMoveWin(board, playerNumber):
    """Checks all columns to see if dropping a piece there would cause a win for playerNumber.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int playerNumber: The player number whose move is being tested.
    :return int: The column index that results in a win, or -1 if none.
    """
    piece = getPlayerPiece(playerNumber)
    cols = len(board[0])

    for col in range(cols):
        row = getOpenRow(board, col)
        if row != -1:
            original = board[row][col]
            board[row][col] = piece
            if checkWinner(board, playerNumber):
                board[row][col] = original
                return col
            board[row][col] = original

    return -1


def checkAdjacent(board, playerNumber):
    """Heuristic AI: chooses among columns where the new piece would be adjacent to existing pieces.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int playerNumber: The player number whose piece this function is to test for adjacent pieces.
    :return int: A column index picked from candidate adjacents, or -1 if not enough candidates.
    """
    col = -1
    piece = getPlayerPiece(playerNumber)
    adjacents = []

    rows = len(board)
    cols = len(board[0])

    for column in range(cols):
        row = getOpenRow(board, column)
        if row != -1:
            # upper left
            if row - 1 >= 0 and column - 1 >= 0:
                if board[row - 1][column - 1] == piece:
                    adjacents.append(column)
            # left
            if column - 1 >= 0:
                if board[row][column - 1] == piece:
                    adjacents.append(column)
            # lower left
            if row + 1 < rows and column - 1 >= 0:
                if board[row + 1][column - 1] == piece:
                    adjacents.append(column)
            # lower
            if row + 1 < rows:
                if board[row + 1][column] == piece:
                    adjacents.append(column)
            # lower right
            if row + 1 < rows and column + 1 < cols:
                if board[row + 1][column + 1] == piece:
                    adjacents.append(column)
            # right
            if column + 1 < cols:
                if board[row][column + 1] == piece:
                    adjacents.append(column)
            # upper right
            if row - 1 >= 0 and column + 1 < cols:
                if board[row - 1][column + 1] == piece:
                    adjacents.append(column)

    if len(adjacents) > 1:
        randVal = random.randrange(0, len(adjacents))
        col = adjacents[randVal]

    return col


def getComputerInput(board, currentPlayerTurn):
    """AI / decision making for the computer in single player mode.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int currentPlayerTurn: The player number for whom its turn it is.
    :return int: col - The column where the computer will place its piece.
    """
    opponentPlayerTurn = switchTurns(currentPlayerTurn)

    col = checkForNextMoveWin(board, currentPlayerTurn)

    if col == -1:
        col = checkForNextMoveWin(board, opponentPlayerTurn)

    if col == -1:
        col = checkAdjacent(board, currentPlayerTurn)

    if col == -1:
        col = random.randrange(0, len(board[0]))
        while getOpenRow(board, col) == -1:
            col = random.randrange(0, len(board[0]))

    print("Player {0}, please select a column between (0-{1}): {2}".format(currentPlayerTurn, len(board[0]) - 1, col))

    return col


def getOpenRow(board, col):
    """Iterates through all the rows of a given column (col), from bottom to top in the gameboard, and returns the first open row it finds.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int col: The column to check.
    :return int: row - The row index of the first empty row from the bottom of the gameboard. It returns -1 if no empty row is found.
    """
    empty = getPlayerPiece(0)
    for row in range(len(board) - 1, -1, -1):
        if board[row][col] == empty:
            return row
    return -1


def placePiece(board, row, col, piece):
    """Inserts a piece into the gameboard a a specific position.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int row: The row on the gameboard to insert the piece into.
    :param int col: The column on the gameboard to insert the piece into.
    :param string piece: The actual piece (should be "X", "O", or ".") to place into the gameboard
    """
    board[row][col] = piece


def dropPieceIntoBoard(board, col, playerNumber):
    """Inserts a piece into the gameboard in a given column.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int col: The column on the gameboard to insert the piece into.
    :param int playerNumber: The player number whose piece this function is to 'drop' into the board.
    """
    row = getOpenRow(board, col)
    placePiece(board, row, col, getPlayerPiece(playerNumber))


def checkDraw(board):
    """Checks if the entire board is filled, implying a draw.

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :return boolean: False if any empty space exists; True otherwise.
    """
    empty = getPlayerPiece(0)
    for row in board:
        for col_val in row:
            if col_val == empty:
                return False
    return True


def checkWinner(board, playerNumber):
    """Checks the gameboard to see if a winning condition is present (4 in a row).

    :param list of lists board: The data structure that contains the contents of the gameboard.
    :param int playerNumber: The player number whose piece this function checks.
    :return boolean: Returns True if a winning condition is found. It returns False otherwise.
    """
    piece = getPlayerPiece(playerNumber)
    rows = len(board)
    cols = len(board[0])

    # horizontal
    for row in range(rows):
        for col in range(cols - 3):
            if (board[row][col] == piece and
                board[row][col + 1] == piece and
                board[row][col + 2] == piece and
                board[row][col + 3] == piece):
                return True

    # vertical
    for row in range(rows - 3):
        for col in range(cols):
            if (board[row][col] == piece and
                board[row + 1][col] == piece and
                board[row + 2][col] == piece and
                board[row + 3][col] == piece):
                return True

    # negative slope diagonals (\)
    for row in range(rows - 3):
        for col in range(cols - 3):
            if (board[row][col] == piece and
                board[row + 1][col + 1] == piece and
                board[row + 2][col + 2] == piece and
                board[row + 3][col + 3] == piece):
                return True

    # positive slope diagonals (/)
    for row in range(3, rows):
        for col in range(cols - 3):
            if (board[row][col] == piece and
                board[row - 1][col + 1] == piece and
                board[row - 2][col + 2] == piece and
                board[row - 3][col + 3] == piece):
                return True

    return False


def resetGameOptions():
    """Reset all the relevant gameplay variables to their pre-gameplay state.

    :return int, boolean, boolean: currentPlayerTurn, winner, draw
    """
    currentPlayerTurn = 1
    winner = False
    draw = False
    return currentPlayerTurn, winner, draw


def switchTurns(currentPlayerTurn):
    """Change the current turn from Player 1 to Player 2 and vice versa.

    :param int currentPlayerTurn:
    :return int: 1 or 2
    """
    return (currentPlayerTurn % 2) + 1


def main():
    """The main function for the game. The primary gameplay loop is located here."""
    running = True

    currentPlayerTurn = 1
    winner = False
    draw = False

    printTitleMaterial()

    while running:
        choice = initialChoice()
        if choice == "p":

            currentPlayerTurn, winner, draw = resetGameOptions()
            numPlayers = chooseNumPlayers()
            board = createBoard(7, 6)

            printBanner()
            printBoard(board)

            while True:
                if numPlayers == 1:
                    if currentPlayerTurn == 1:
                        col = getHumanInput(board, currentPlayerTurn)
                    elif currentPlayerTurn == 2:
                        col = getComputerInput(board, currentPlayerTurn)
                    else:
                        print("ERROR: currentPlayerTurn is neither 1 or 2! It is actually: {0}".format(currentPlayerTurn))
                        sys.exit()
                elif numPlayers == 2:
                    col = getHumanInput(board, currentPlayerTurn)
                else:
                    print("ERROR: numPlayers is neither 1 or 2! It is actually: {0}".format(numPlayers))
                    sys.exit()

                dropPieceIntoBoard(board, col, currentPlayerTurn)
                printBoard(board)

                winner = checkWinner(board, currentPlayerTurn)
                draw = checkDraw(board)

                if winner:
                    print("~~ Player {0} ({1}) Wins! ~~".format(currentPlayerTurn, getPlayerPiece(currentPlayerTurn)))
                    print()
                    break
                elif draw:
                    print("~~ Draw! ~~")
                    print()
                    break
                else:
                    print("~~ End Of Player {0} ({1}) Turn ~~".format(currentPlayerTurn, getPlayerPiece(currentPlayerTurn)))
                    print()
                    currentPlayerTurn = switchTurns(currentPlayerTurn)

        elif choice == "i":
            print("\nInstructions:")
            print("• Players take turns dropping pieces into columns (0–6).")
            print("• Pieces fall to the lowest available row in that column.")
            print("• First player to connect four of their pieces")
            print("  horizontally, vertically, or diagonally wins.")
            print("• If the board fills up with no winner, it's a draw.\n")

        elif choice == "q":
            print("Goodbye!")
            running = False

        else:
            print("ERROR: Variable 'choice' should have been 'p', 'i', or 'q', but instead was:", choice)
            quit()


if __name__ == "__main__":
    main()