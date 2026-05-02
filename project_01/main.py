import random

MAX_LINES = 3

COLUMNS = 3
ROWS = 10

symbol_count = {
    "A": 20,
    "B": 10,
    "C": 30,
    "D": 40,
}

symbol_values = {
    "A": 4,
    "B": 2,
    "C": 2,
    "D": 1,
}

def arrange():
    columns = []
    symbols = []
    for el, i in symbol_count.items():
        for _ in range(i):
            symbols.append(el)
    for _ in range(COLUMNS):
        column = []
        for _ in range(ROWS):
            sym = random.choice(symbols)
            symbols.remove(sym)
            column.append(sym)
        columns.append(column)

    return columns

def print_round(columns):
    for row in range(1, 4):
        for col in range(COLUMNS):
            if col < COLUMNS - 1:
                print(columns[col][-row], end=' | ')
            else:
                print(columns[col][-row])

def check_win(columns, bet, lines):
    winning_amount = 0
    for line in range(lines):
        winning_line = 0
        symbol_to_check = columns[0][-line - 1]
        for i in range(COLUMNS):
            if columns[i][-line - 1] != symbol_to_check:
                break
        else:
            print(f"You win on line {line + 1}")
            winning_line += symbol_values[symbol_to_check] * COLUMNS
            winning_amount += winning_line * bet

    return winning_amount

def balance():
    while True:
        amount = input("Enter starting amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("There must be some positive amount")
        else:
            print("Enter valid amount")

    return amount

def how_many_lines():
    while True:
        lines = input(f"On how many lines do you bet (1 - {MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Lines must be in specified range")
        else:
            print("Enter valid number")

    return lines

def bet_per_line(lines, amount):
    while True:
        bpl = input("What is your bet per line: $")
        if bpl.isdigit():
            bpl = int(bpl)
            if 0 == bpl:
                print("There must be some positive bet")
            elif bpl * lines > amount:
                print("You don't have enough money for that bet")
            else:
                break
        else:
            print("Enter valid number")

    return bpl

def spin(bet, lines):
    curr = arrange()
    print_round(curr)
    win = check_win(curr, bet, lines)

    return win

def main():
    bal = balance()
    while True:
        print(f"Current balance is: ${bal}")
        if input("Press Enter to play (q to quit) ") == 'q':
            break
        lines = how_many_lines()
        bpl = bet_per_line(lines, bal)
        bet = bpl * lines
        win = spin(bpl, lines)
        bal += win - bet
        if bal == 0:
            print("You are out of money!")
            break

if __name__ == "__main__":
    main()