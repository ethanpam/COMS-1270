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
            return

def candyRealm():
    players = [
        {'name': 'Bot1' ,'Bot' : True, 'tile': 1},
        {'name': 'Bot2' ,'Bot' : True, 'tile': 1},
        {'name': 'Bot3' ,'Bot' : True, 'tile': 1},
        {'name': 'Bot4' ,'Bot' : True, 'tile': 1}
    ]
    while True:
        for i in range(int(input("How many human player? [1-4]: "))):
            player = input(f"What is the name of player {i + 1}: ")
            players[i]['name'] = player
            players[i]['Bot'] = False
        break
    for t in range(4):
        print(f"\rShuffling player order{t*'.'}", end='')
        time.sleep(1)
    random.shuffle(players)
    print(f"Player Order:\n")
    return print(players)



def main():
    printTitleMaterial()
    while True:
        print("-----------------------")
        choice = input("MAIN MENU: [p]lay game, [i]nstructions, or [q]uit: ")
        if choice == "p":
            candyRealm()
        elif choice == "i":
            instruction()
        elif choice == "q":
            print("\nHave a good day, goodbye!\n")
            return

if __name__ == "__main__":
    main()