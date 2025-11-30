# Ethan Pham          11/27/25
# Assignment #6
#
# A digital version of the classic board game "Candy Land."
# Players take turns drawing colored cards to move across a randomized board.
# The goal is to reach the GOAL tile before the other players.

import random
import time

def printTitleMaterial():
    print("Candy Realm!\n")
    print("By: Ethan Pham")
    print("COMS-1270 4")

def instruction():
    print("\nGAME INSTRUCTION")
    print("----------------")
    print("Goal:")
    print("Be the first player to travel across the Candy Realm board and reach the GOAL space.\n")
    print("How to Play:")
    print("- Play with four players, either bots or human players.")
    print("- Each player takes a turn. On your turn, you may draw a card, shuffle the deck, or return to the main menu.")
    print("- The deck contains colored cards (R, P, Y, B, O, G).")
    print("- Before the game begins, you choose how many copies of each color card are added to the deck.")
    print("- When the deck runs out of cards, it is reshuffled automatically.\n")
    print("Movement Rules:")
    print("- When you draw a colored card, you move forward to the NEXT tile with that color.")
    print("- If there are no more tiles of that color ahead of you, you cannot move and the drawn card is discarded.")
    print("- If you are already on the final colored tile, ANY card you draw will move you into the GOAL space and you win.\n")
    while True:
        if input("Enter [back] to return to main menu: ").lower() == "back":
            return main()

def shuffling(word, shuffle):
    for t in range(4):
        print(f"\rShuffling {word}{t*'.'}", end='')
        time.sleep(.5)
    random.shuffle(shuffle)
    print()
    return shuffle

def checkEmpty(deck, copies):
    if len(deck) == 0:
        deck[:] = card(copies)
        return deck

def card(copies):
    deck = []
    print("Adding Cards")
    for _ in range(copies):
        deck.append("R")
        deck.append("P")
        deck.append("Y")
        deck.append("B")
        deck.append("O")
        deck.append("G")
    deck = shuffling("deck", deck)
    return deck

def buildBoard():
    board = []
    for _ in range(3):
        board.append("R")
        board.append("P")
        board.append("Y")
        board.append("B")
        board.append("O")
        board.append("G")
    random.shuffle(board)
    board.append("GOAL!")
    return board

def playerAssign():
    players = [
        {'name': 'Bot1' ,'Bot' : True, 'tile': 0},
        {'name': 'Bot2' ,'Bot' : True, 'tile': 0},
        {'name': 'Bot3' ,'Bot' : True, 'tile': 0},
        {'name': 'Bot4' ,'Bot' : True, 'tile': 0}
    ]
    while True:
        try:
            count = int(input("How many human player? [1-4]: "))
            if 1 <= count <= 4:
                break
            else:
                print("Enter value between 1-4")
        except ValueError:
            print("Invalid input")
    for i in range(int(count)):
        while True:
            player = input(f"What is the name of player {i + 1}: ")
            if len(player) > 7:
                print("Player name is too long")
            else:
                players[i]['name'] = player
                players[i]['Bot'] = False
                break
    shuffling("player order", players)
    print(f"\nPlayer Order:\n1.{players[0]['name']}\n2.{players[1]['name']}\n3.{players[2]['name']}\n4.{players[3]['name']}")
    return players

def playingBoard(players, deck, board):
    print("-------------------------------------------------------------------------------------------")
    print(f"{players[0]['name']:>{4 * players[0]['tile'] + 7}}")
    print(f"{players[1]['name']:>{4 * players[1]['tile'] + 7}}")
    print(f"{players[2]['name']:>{4 * players[2]['tile'] + 7}}")
    print(f"{players[3]['name']:>{4 * players[3]['tile'] + 7}}")
    print(f"{"START":>7}",end='')
    for title in board[:18]:
        print(f"{title:>4}", end='')
    print(f"{"GOAL!":>8}",end='')
    print()
    print(f"{"CARDS":>7}", end='')
    for card in deck[:18]:
        print(f"{card:>4}", end='')
    print()
    return

def turn(players, deck, copies, board):
    playerTurn = 0
    while True:
        checkEmpty(deck, copies)
        playingBoard(players, deck, board)
        if players[playerTurn]["Bot"]:
            print(f"{players[playerTurn]["name"]} thinking...")
            time.sleep(1)
            choice = botChoice(players, deck, playerTurn, board)
            if choice == 'd':
                drawingcard = deck[0]  
                time.sleep(random.choice([.5, 2.5]))
                print(f"{players[playerTurn]["name"]} chooses to draw {drawingcard} card.")
                won = draw(players, deck, playerTurn, copies, board)
                if won:
                    players[playerTurn]['tile'] = 20
                    playingBoard(players, deck, board)
                    return main()
                else:
                    time.sleep(1)
            elif choice == 's':
                print(f"{players[playerTurn]["name"]} chooses to shuffle the deck")
                shuffling("deck", deck)
        else:
            choice = input(f"{players[playerTurn]["name"]}: Would you like to [d]raw a {deck[0]} card, [s]huffle the deck, or [q]uit: ")
            if choice.lower() == "d":
                drawingcard = deck[0]  
                print(f"{players[playerTurn]["name"]} chooses to draw {drawingcard} card.")
                won = draw(players, deck, playerTurn, copies, board)
                if won:
                    players[playerTurn]['tile'] = 20
                    playingBoard(players, deck, board)
                    return main()
            elif choice.lower() == "s":
                shuffling("deck", deck)
            elif choice.lower() == "q":
                return main()
            else:
                print("Invalid Input")
                continue
        playerTurn += 1
        if playerTurn >= 4:
            playerTurn = 0

def botChoice(players, deck, playerTurn, board):
    drawingCard = deck[0]
    for i in range(len(board)):
        if players[playerTurn]['tile'] + i < len(board) and board[players[playerTurn]['tile'] + i] == drawingCard:
            return 'd'
    if random.random() < .35:
        return 's'
    else:
        return 'd'

def draw(players, deck, playerTurn, copies, board):
    checkEmpty(deck, copies)
    position = players[playerTurn]["tile"]
    last_color_tile = len(board) - 1
    goal_tile = len(board)
    if position == last_color_tile:
        players[playerTurn]["tile"] = goal_tile
        print(f"{players[playerTurn]['name']} won!")
        del deck[0]
        return True
    card = deck[0]
    while True:
        position += 1
        if position > last_color_tile:
            print(f"{players[playerTurn]['name']} cannot move with {card}.")
            print(f"Removing {card} from deck")
            del deck[0]
            return False
        if board[position - 1] == card:
            players[playerTurn]["tile"] = position
            del deck[0]
            return False

def candyRealm():
    players = playerAssign()
    while True:
        try:
            copies = int(input("How many copies of each cards [1-5]?: "))
            if 1 <= copies <= 5:
                break
            else:
                print("Enter a value between [1-5]")
        except ValueError:
            print("Invalid Input")
    deck = card(copies)
    board = buildBoard()
    turn(players, deck, copies, board)

def main():
    printTitleMaterial()
    while True:
        print("----------------------------------------------------")
        choice = input("MAIN MENU: [p]lay game, [i]nstructions, or [q]uit: ")
        if choice.lower() == "p":
            candyRealm()
            return
        elif choice.lower() == "i":
            instruction()
            return
        elif choice.lower() == "q":
            print("\nHave a good day, goodbye!\n")
            return
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()