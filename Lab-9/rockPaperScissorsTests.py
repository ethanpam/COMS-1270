# Ethan Pham — Lab 9 — rockPaperScissors tests

import pytest

from rockPaperScissors import (
    generateComputerMove,
    determineWinner,
    playRound,
)


def test_generate_computer_move_uses_choice(monkeypatch):
    def fake_choice(options):
        return options[0]

    monkeypatch.setattr("rockPaperScissors.random.choice", fake_choice)
    assert generateComputerMove() == "Rock"


@pytest.mark.parametrize(
    "player,computer,expected",
    [
        ("Rock", "Scissors", "Rock"),
        ("Paper", "Rock", "Paper"),
        ("Scissors", "Paper", "Scissors"),
        ("Rock", "Paper", "Paper"),
        ("Paper", "Scissors", "Scissors"),
        ("Scissors", "Rock", "Rock"),
        ("Rock", "Rock", "Draw"),
    ],
)
def test_determine_winner(player, computer, expected):
    assert determineWinner(player, computer) == expected


def test_determine_winner_rejects_invalid_move():
    with pytest.raises(ValueError):
        determineWinner("Lizard", "Rock")
    with pytest.raises(ValueError):
        determineWinner("Rock", "Spock")


def test_play_round_player_wins(monkeypatch):
    monkeypatch.setattr("rockPaperScissors.generateComputerMove", lambda: "Scissors")
    assert playRound("Rock") == "Player Wins!"


def test_play_round_computer_wins(monkeypatch):
    monkeypatch.setattr("rockPaperScissors.generateComputerMove", lambda: "Paper")
    assert playRound("Rock") == "Computer Wins!"


def test_play_round_draw(monkeypatch):
    monkeypatch.setattr("rockPaperScissors.generateComputerMove", lambda: "Paper")
    assert playRound("Paper") == "Draw!"


def test_play_round_rejects_invalid_move():
    with pytest.raises(ValueError):
        playRound("Lizard")
