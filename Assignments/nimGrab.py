#Ethan Pham            10-10-25
#Assignment #3
#
#This uses loop, function, conditional logic, random module

import random

print("NIMGRAB!\n\nBy: Ethan Pham\n[COMS-1270 4]\n")

def play(playerMode):
    sticks = 20
    if playerMode == "h":
        currentTurn = "Player 1"
    else:
        currentTurn = "Human"
    while sticks > 0:
        print(f"\nCurrent Items left: {sticks}\n", '|'*sticks)
        if currentTurn == "Player 1" or currentTurn == "Human":
            while True:
                takeSticks = int(input(f"\n{currentTurn}, how many sticks would you like to take [1-3]?: "))
                if takeSticks not in range(1,4):
                    print("Invalid input")
                elif takeSticks > sticks:
                    print("You can't take more sticks than what remains")
                else:
                    break
            before = sticks
            sticks = removeSticks(sticks, takeSticks, playerMode, currentTurn)
            if playerMode == "c":
                human_after = before - takeSticks
                if human_after <= 0:
                    print("You took the last stick so computer wins")
                    break
                if sticks <= 0:
                    print("Computer took the last stick so you win! Wow!")
                    break
                continue
            else:
                if sticks == 0:
                    print(f"{currentTurn} took the last stick so they lost!")
                    break
                if currentTurn == "Player 1":
                    currentTurn = "Player 2"
                else:
                    currentTurn = "Player 1"
        else:
            while True:
                takeSticks = int(input("\nPlayer 2, how many sticks would you like to take [1-3]: "))
                if takeSticks not in range(1,4):
                    print("Invalid input")
                elif takeSticks > sticks:
                    print("You can't take more sticks than what remains")
                else:
                    break
            before = sticks
            sticks = removeSticks(sticks, takeSticks, playerMode, currentTurn)
            if sticks == 0:
                print("\nPlayer 2 took the last stick so they lost!")
                print("Player 1 wins!")
                break
            currentTurn = "Player 1"

def rules():
    print("Rules")
    print("-The game starts off with 20 sticks")
    print("-Players each take turn removing 1-3 sticks")
    print("-Taking sticks beyond the range of 1-3 is invalid")
    print("-This game can be played in either 2-player mode or against a computer")
    print("-The player who takes the LAST stick LOSES")
    print("-Last but not least, HAVE FUN\n")
    main()


def removeSticks(sticks,takesticks, playerMode, currentTurn):
    sticks = sticks - takesticks
    print(f"\n{currentTurn} took {takesticks} sticks")
    print(f"Items left: {sticks}")
    print(f"{'|' * sticks}")
    if playerMode == "c" and sticks > 0:
        takesticks = min(random.randrange(1,4), sticks)
        sticks = sticks - takesticks
        print(f"\nComputer took {takesticks} sticks")
        print(f"Items left: {sticks}")
        print(f"{'|' * sticks}")
    return(sticks)

def main():
    while True:
        menu = str(input("Do you want to [p]lay, read the [r]ules, or [q]uit?: "))
        if menu == "p":
            while True:
                playerMode = str(input("Do you want to play against [h]uman or [c]omputer?: "))
                if playerMode == "h" or playerMode == "c":
                    return play(playerMode)
                else:
                    print("Invalid input")
        elif menu == "r":
            rules()
            return
        elif menu == "q":
            print("Goodbye!")
            return
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()

