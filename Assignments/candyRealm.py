# Ethan Pham          7-19-2024
# Assignment #6
#
# This is an digital verison of the classic popular game called 'Candy Land'

import random
import time

def printTitleMaterial():
    print("Candy Realm!\n")
    print("By: Ethan Pham")
    print("COMS-1270 4")

def instruction():
    print("\nGAME INSTRUCTION")
    print("----------------")
    print("Goal:\nBe the first player to travel across the Candy Realm board and reach the GOAL space\n")
    print("How to play:")
    print("-Play with four players, either bots or human players")
    print("-Each player takes a turn\nOn the players turn, they may draw or shuffle the deck or even quit to main menu")
    print("-The deck itself contains colored cards")
    print("-The number of copies of each card is chosen before the game begins")
    print("-When the deck runs out, it is reshuffled automatically")
    while True:
        if input("\nEnter [back] to return to main menu: ") == "back":
            return main()

def shuffling(word, shuffle):
    for t in range(4):
        print(f"\rShuffling {word}{t*'.'}", end='')
        time.sleep(.5)
    random.shuffle(shuffle)
    print()
    return shuffle

def playerAssign():
    players = [
        {'name': 'Bot1' ,'Bot' : True, 'tile': 1},
        {'name': 'Bot2' ,'Bot' : True, 'tile': 1},
        {'name': 'Bot3' ,'Bot' : True, 'tile': 1},
        {'name': 'Bot4' ,'Bot' : True, 'tile': 1}
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
            player = input(f"What is the name of player {i + 1}: ")
            players[i]['name'] = player
            players[i]['Bot'] = False
    player = shuffling("player order", players)
    print(f"\nPlayer Order:\n1.{players[0]['name']}\n2.{players[1]['name']}\n3.{players[2]['name']}\n4.{players[3]['name']}")
    return players

def card():
    deck = []
    while True:
        try:
            copies = int(input("How many copies of each cards [1-5]?: "))
            if 1 <= copies <= 5:
                break
            else:
                print("Enter a value between [1-5]")
        except ValueError:
            print("Invalid Input")
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

def playingBoard(players, deck):
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
    print(f"{players[0]["name"]:>11}")
    print(f"{players[1]["name"]:>11}")
    print(f"{players[2]["name"]:>11}")
    print(f"{players[3]["name"]:>11}")
    print(f"{"START":>7}",end='')
    for title in board[:18]:
        print(f"{title:>4}", end='')
    print(f"{"GOAL!":>7}",end='')
    print()
    print(f"{"CARDS":>7}", end='')
    for card in deck[:18]:
        print(f"{card:>4}", end='')
    print()

def turn(players, deck):
    playerTurn = 0
    while True:
        playingBoard(players, deck)
        choice = input(f"{players[playerTurn]["name"]}: Would you like to [d]raw a {deck[0]} card, [s]huffle the deck, or [q]uit: ")
        if choice.lower() == "d":
            draw(players, deck)
        elif choice.lower() == "s":
            shuffling("deck", deck)
        elif choice.lower() == "q":
            return main()
        playerTurn += 1
        if playerTurn >= len(players):
            playerTurn = 0

def draw(players, deck):
    pass

def candyRealm():
    players = playerAssign()
    deck = card()
    turn(players, deck)

def main():
    while True:
        print("-----------------------")
        choice = input("MAIN MENU: [p]lay game, [i]nstructions, or [q]uit: ")
        if choice == "p":
            candyRealm()
            return
        elif choice == "i":
            instruction()
            return
        elif choice == "q":
            print("\nHave a good day, goodbye!\n")
            return

if __name__ == "__main__":
    printTitleMaterial()
    main()