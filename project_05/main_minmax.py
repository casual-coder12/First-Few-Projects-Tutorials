import math


def check_win(table):
    winning_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for line in winning_lines:
        if table[line[0]] == table[line[1]] == table[line[2]] != "":
            return table[line[0]]
    return None if "" in table else "Tie"


def minimax(table, depth, is_max):
    rezultat = check_win(table)
    if rezultat == "O": return 1
    if rezultat == "X": return -1
    if rezultat == "Tie": return 0

    if is_max:
        best_score = -math.inf
        for i in range(9):
            if table[i] == "":
                table[i] = "O"
                score = minimax(table, depth + 1, False)
                table[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if table[i] == "":
                table[i] = "X"
                score = minimax(table, depth + 1, True)
                table[i] = ""
                best_score = min(score, best_score)
        return best_score


def best_move(table):
    best_score = -math.inf
    move = 0
    for i in range(9):
        if table[i] == "":
            table[i] = "O"
            score = minimax(table, 0, False)
            table[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move


def print_board(table):
    for i in range(0, 9, 3):
        print(f"{table[i] or i} | {table[i + 1] or i + 1} | {table[i + 2] or i + 2}")
        if i < 6:
            print("--+---+--")

def main():
    # Main loop
    table = [""] * 9
    print("You are playing against AI (You are X). Enter the number of the field (0-8):")

    while True:
        print_board(table)
        if check_win(table):
            break

        player_move = int(input("Your move: "))
        if table[player_move] == "":
            table[player_move] = "X"
            if check_win(table):
                break

            print("\nAI is thinking...")
            table[best_move(table)] = "O"
        else:
            print("The field is occupied!")

    print(f"\nEND! {'It was a tie!' if check_win(table) == 'Tie' else f'The winner is {check_win(table)}!'}")

if __name__ == "__main__":
    main()
