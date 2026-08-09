ROWS = 6
COLS = 7

board = [["." for _ in range(COLS)] for _ in range(ROWS)]


def print_board():
    print()
    for row in board:
        print(" ".join(row))
    print("1 2 3 4 5 6 7")
    print()


def drop_piece(column, piece):
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == ".":
            board[row][column] = piece
            return row
    return -1


def check_winner(row, col, piece):
    directions = [
        (0, 1),   # horizontal
        (1, 0),   # vertical
        (1, 1),   # diagonal
        (1, -1)   # other diagonal
    ]

    for dr, dc in directions:
        count = 1

        # Check one direction
        r, c = row + dr, col + dc
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == piece:
            count += 1
            r += dr
            c += dc

        # Check opposite direction
        r, c = row - dr, col - dc
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == piece:
            count += 1
            r -= dr
            c -= dc

        if count >= 4:
            return True

    return False


def board_full():
    return all(board[0][col] != "." for col in range(COLS))


def play_game():
    player = "X"

    while True:
        print_board()

        try:
            column = int(input(f"Player {player}, choose a column (1-7): ")) - 1
        except ValueError:
            print("Please enter a number from 1 to 7.")
            continue

        if column < 0 or column >= COLS:
            print("Choose a column from 1 to 7.")
            continue

        row = drop_piece(column, player)

        if row == -1:
            print("That column is full!")
            continue

        if check_winner(row, column, player):
            print_board()
            print(f"Player {player} wins! 🎉")
            break

        if board_full():
            print_board()
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"


play_game()








