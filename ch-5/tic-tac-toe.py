import random
import time

board = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-'
]
turn = 0
players = [
    {
        'name': '',
        'symbol': '',
        'turn': ''
    },
    {
        'name': '',
        'symbol': '',
        'turn': ''
    }
]

p1Symbol = 'O'
p2Symbol = 'X'

def display_board():
    for i, itm in enumerate(board):
        if i in [3, 6]:
            print("---|---|---")
        print(f" {itm} ", end="")
        print("\n" if (i + 1) % 3 == 0 else "|", end="")
    print()


def check_win(symbol):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]               # Diagonal
    ]
    # for condition in win_conditions:
    #     if all(board[i] == symbol for i in condition):
    #         return True
    # return False
    return any(
        all(board[i] == symbol for i in condition)
        for condition in win_conditions
    )

def check_draw():
    return '-' not in board


print()
print("Enter first player name:")
players[0]['name'] = input()
# Heli
print(f"Hello {players[0]['name']}")

print("Enter second player name:")
players[1]['name'] = input()
# Uri
print(f"Hello {players[1]['name']}")

print("... Start the game with touch ...")
print("Waiting for touch result...")
time.sleep(1)

turn = random.randint(0, 1)
print(f"{players[turn]['name']} won the touch.")

while True:
    print("Select O or X")
    players[turn]['symbol'] = input()

    if players[turn]['symbol'] not in ['O', 'X']:
        print("Select from O or X\n")
    else:
        if turn == 0:
            players[1]['symbol'] = "X" if players[0]['symbol'] == "O" else "O"
        else:
            players[0]['symbol'] = "X" if players[1]['symbol'] == "O" else "O"
        break

print(f"{players[0]['name']} select {players[0]['symbol']} and {players[1]['name']} select {players[1]['symbol']}")
print(players)



while True:
    display_board()
    print(f"{players[turn]['name']}'s turn ({players[turn]['symbol']})")

    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == '-':
                board[move] = players[turn]['symbol']
                break
            else:
                print("That space is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number from 1 to 9.")

    if check_win(players[turn]['symbol']):
        display_board()
        print(f"Congratulations {players[turn]['name']}! You win!")
        break
    if check_draw():
        display_board()
        print("It's a draw!")
        break

    turn = 1 - turn  