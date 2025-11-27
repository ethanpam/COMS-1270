# Ethan Pham — Lab 9 — fourInSequence tests

import pytest

from fourInSequence import (
    checkAdjacent,
    checkDraw,
    checkForNextMoveWin,
    checkWinner,
    createBoard,
    getPlayerPiece,
    placePiece,
)


def test_check_for_next_move_win_finds_horizontal_win():
    board = createBoard(7, 6)
    for col in range(3):
        board[5][col] = "X"
    assert checkForNextMoveWin(board, 1) == 3


def test_check_for_next_move_win_returns_negative_when_no_win():
    board = createBoard(7, 6)
    assert checkForNextMoveWin(board, 1) == -1


def test_check_adjacent_picks_from_candidates(monkeypatch):
    board = createBoard(4, 4)
    for row in range(4):
        board[row][0] = "X"
    board[3][1] = "X"
    board[3][2] = "X"

    def fake_randrange(start, stop):
        return 0

    monkeypatch.setattr("fourInSequence.random.randrange", fake_randrange)
    assert checkAdjacent(board, 1) == 1


def test_check_adjacent_returns_negative_with_one_candidate(monkeypatch):
    board = createBoard(1, 2)
    board[1][0] = "X"

    def fake_randrange(start, stop):
        return 0

    monkeypatch.setattr("fourInSequence.random.randrange", fake_randrange)
    assert checkAdjacent(board, 1) == -1


def test_check_draw_true_when_board_full():
    board = createBoard(4, 4)
    for row in range(4):
        for col in range(4):
            board[row][col] = "X"
    assert checkDraw(board) is True


def test_check_draw_false_when_empty_exists():
    board = createBoard(3, 3)
    board[2][0] = "X"
    assert checkDraw(board) is False


def test_check_winner_horizontal_vertical_and_diagonal():
    board = createBoard(7, 6)
    for c in range(4):
        board[5][c] = "X"
    assert checkWinner(board, 1) is True

    board = createBoard(7, 6)
    for r in range(4):
        board[5 - r][0] = "O"
    assert checkWinner(board, 2) is True

    board = createBoard(7, 6)
    for offset in range(4):
        row = 5 - offset
        col = offset
        board[row][col] = "X"
    assert checkWinner(board, 1) is True

    board = createBoard(7, 6)
    for offset in range(4):
        row = offset
        col = offset
        board[row][col] = "O"
    assert checkWinner(board, 2) is True


def test_check_winner_false_when_no_connect_four():
    board = createBoard(7, 6)
    placePiece(board, 5, 0, getPlayerPiece(1))
    placePiece(board, 5, 1, getPlayerPiece(2))
    placePiece(board, 5, 2, getPlayerPiece(1))
    placePiece(board, 5, 3, getPlayerPiece(2))
    assert checkWinner(board, 1) is False
