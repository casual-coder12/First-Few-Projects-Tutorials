import random

LINES = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

def print_board(board):
    for i, row in enumerate(board):
        row_str = " "
        for j, elem in enumerate(row):
            row_str += elem
            if j != len(row) - 1:
                row_str += " | "
        print(row_str)
        if i != len(board) - 1:
            print("-----------")

def get_move(turn, board):
    while True:
        try:
            row = int(input("Row: "))
            col = int(input("Column: "))
            if board[row - 1][col - 1] == " ":
                return row - 1, col - 1
            else:
                print("Incorrect move")
        except (ValueError, TypeError):
            print("Enter valid numbers")
        except IndexError:
            print("Numbers must be between 1-3")

def computer_move(turn, board, lines_signs):
    op_turn = "X" if turn == "O" else "O"
    free_line_ind = []
    for i, line in enumerate(lines_signs):
        if sorted(line) == [" ", turn, turn]:
            return LINES[i][line.index(" ")]
    for i, line in enumerate(lines_signs):
        if sorted(line) == [" ", op_turn, op_turn]:
            return LINES[i][line.index(" ")]
        elif line == [" ", " ", " "]:
            free_line_ind.append(i)
    if free_line_ind:
        ind = random.choice(free_line_ind)
        print(LINES[ind][random.randint(0,2)], "rand")
        return LINES[ind][random.randint(0,2)]
    else:
        indexes_of_lines = [i for i, line in enumerate(lines_signs) if " " in line]
        ind = random.choice(indexes_of_lines)
        line = LINES[random.choice(indexes_of_lines)]
        indexes_of_empty_spaces = [i for i, el in enumerate(lines_signs[ind]) if el == " "]
        return line[random.choice(indexes_of_empty_spaces)]

def move(turn, board, place, lines_signs):
    row = place[0]
    col = place[1]
    board[row][col] = turn
    for i, line in enumerate(LINES):
        for j in range(3):
            if board[line[j][0]][line[j][1]] != " ":
                lines_signs[i][j] = board[line[j][0]][line[j][1]]

def check_win(board):
    for line in LINES:
        if board[line[0][0]][line[0][1]] == board[line[1][0]][line[1][1]] == board[line[2][0]][line[2][1]] != " ":
            return board[line[0][0]][line[0][1]]

    return None

def check_win_alt(board):
    for row in board:
        if set(row) == {"X"}:
            return "X"
        if set(row) == {"O"}:
            return "O"
    for col in zip(*board):
        if set(col) == {"X"}:
            return "X"
        if set(col) == {"O"}:
            return "O"
    if (board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ") or \
        (board[0][2] == board[1][1] == board[2][0] and board[0][2] != " "):
        return board[1][1]

    return None

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

lines_signs = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def main():
    print_board(board)
    player = input("What would you like to be? (X/O)").upper()
    turn_number = 0
    while turn_number < 9:
        turn = "O" if turn_number % 2 else "X"
        print(f"It is the {turn}'s turn, select your move.")
        place = get_move(turn, board) if turn == player else computer_move(turn, board, lines_signs)
        move(turn, board, place, lines_signs)
        turn_number += 1
        print_board(board)
        if winner := check_win(board):
            print(f"The winner is {winner}!")
            break

    if not check_win(board):
        print("It was tie.")

if __name__ == "__main__":
    main()