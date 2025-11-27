# Ethan Pham — 11/18/2024 — Lab 9 — Rock Paper Scissors game

import random

MOVES = ("Rock", "Paper", "Scissors")
WIN_MAP = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper",
}


def _normalize_move(move):
    move = move.strip().capitalize()
    if move not in MOVES:
        raise ValueError("Move must be Rock, Paper, or Scissors.")
    return move


def generateComputerMove():
    return random.choice(MOVES)


def determineWinner(player_move, computer_move):
    player_choice = _normalize_move(player_move)
    computer_choice = _normalize_move(computer_move)
    if player_choice == computer_choice:
        return "Draw"
    if WIN_MAP[player_choice] == computer_choice:
        return player_choice
    return computer_choice


def playRound(player_move):
    player_choice = _normalize_move(player_move)
    computer_choice = generateComputerMove()
    result = determineWinner(player_choice, computer_choice)
    if result == "Draw":
        return "Draw!"
    if result == player_choice:
        return "Player Wins!"
    return "Computer Wins!"


def _get_rounds():
    while True:
        try:
            rounds = int(input("How many rounds would you like to play? (odd number): "))
            if rounds > 0 and rounds % 2 == 1:
                return rounds
        except ValueError:
            pass
        print("ERROR: Please enter a positive odd number.")


def _get_player_move():
    while True:
        move = input("Choose Rock, Paper, or Scissors: ")
        try:
            return _normalize_move(move)
        except ValueError:
            print("ERROR: Invalid move. Please try again.")


def main():
    print("Rock Paper Scissors — Best of Odd Rounds")
    rounds_to_play = _get_rounds()
    needed_wins = rounds_to_play // 2 + 1
    player_wins = 0
    computer_wins = 0
    round_number = 1

    while player_wins < needed_wins and computer_wins < needed_wins:
        print(f"\nRound {round_number}")
        player_move = _get_player_move()
        computer_move = generateComputerMove()
        outcome = determineWinner(player_move, computer_move)
        print(f"Computer chose: {computer_move}")

        if outcome == "Draw":
            print("It's a draw!")
        elif outcome == player_move:
            player_wins += 1
            print("Player wins the round!")
        else:
            computer_wins += 1
            print("Computer wins the round!")

        print(f"Score => Player: {player_wins} | Computer: {computer_wins}")
        round_number += 1

    if player_wins > computer_wins:
        print("\nPlayer wins the match!")
    else:
        print("\nComputer wins the match!")


if __name__ == "__main__":
    main()
