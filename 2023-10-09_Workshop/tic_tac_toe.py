def is_valid_sign(sign):
    if sign in "XO":
        return True
    return False


def is_valid_choice(some_board, some_mapper, some_choice):
    if not some_choice.isdigit():
        print("This is not a number!")
        return False
    some_choice = int(some_choice)
    if some_choice not in some_mapper:
        print(f"Wrong position!")
        return False
    if some_board[mapper[some_choice][0]][mapper[some_choice][1]] != " ":
        print(f"Position already taken!")
        return False
    return True


def render_board(some_board):
    for row in some_board:
        print("| ", end="")
        print(" | ".join([el for el in row if el != '0']), end="")
        print(" |")


def is_row_win(some_board):
    for row in some_board:
        if len(set(row)) == 1 and set(row) != {' '}:
            return True
    return False


def is_row_win_possible(some_board):
    if all(['X' in row and 'O' in row for row in some_board]):
        return False
    return True


def is_column_win_possible(some_board):
    columns = []
    for col in range(len(some_board)):
        current_column = []
        for row in range(len(some_board)):
            current_column.append(some_board[row][col])
        columns.append(current_column)
    if all(['X' in col and 'O' in col for col in columns]):
        return False
    return True


def is_diagonal_win_possible(some_board):
    diagonal_1, diagonal_2 = [], []
    for index in range(len(some_board)):
        diagonal_1.append(some_board[index][index])
        diagonal_2.append(some_board[index][len(some_board) - 1 - index])
    if 'X' in diagonal_1 and 'O' in diagonal_1 and 'X' in diagonal_2 and '0' in diagonal_2:
        return False
    return True


def is_column_win(some_board, some_sign):
    for col in range(len(some_board)):
        current_column = []
        for row in range(len(some_board)):
            current_column.append(some_board[row][col] == some_sign)
        if all(current_column):
            return True
    return False


def is_diagonal_win(some_board, some_sign):
    diagonal_1, diagonal_2 = [], []
    for index in range(len(some_board)):
        diagonal_1.append(some_board[index][index] == some_sign)
        diagonal_2.append(some_board[index][len(some_board) - 1 - index] == some_sign)
    return all(diagonal_1) or all(diagonal_2)


def is_win(some_board, some_sign):
    if any([is_row_win(some_board), is_column_win(some_board, some_sign), is_diagonal_win(some_board, some_sign)]):
        return True
    return False


def is_draw(some_board):
    if any([is_row_win_possible(some_board), is_column_win_possible(some_board), is_column_win_possible(some_board)]):
        return False
    return True


player_one = input("Player one name: ").strip()
player_two = input("Player two name: ").strip()
BOARD_SIZE = 3
board = [[' '] * BOARD_SIZE for _ in range(BOARD_SIZE)]
mapper = {i + 1: (i // BOARD_SIZE, i % BOARD_SIZE) for i in range(BOARD_SIZE ** 2)}

while True:
    player_one_sign = input(f"{player_one} would you like to play with 'X' or 'O'? ").upper()
    if is_valid_sign(player_one_sign):
        break
    else:
        print("Please, enter 'X' or 'O'")
player_two_sign = "X" if player_one_sign == "O" else "O"


print("This is the numeration of the board:")
[print(f"| {' | '.join([str(i + 1 + row * BOARD_SIZE)for i in range(BOARD_SIZE)])} |")for row in range(BOARD_SIZE)]
print(f"{player_one} starts first!")

turn = 1

while True:
    current_player = player_one if turn % 2 != 0 else player_two
    current_sign = player_one_sign if turn % 2 != 0 else player_two_sign
    while True:
        choice = input(f"{current_player} choose a free position [1-{BOARD_SIZE ** 2}]: ").strip()
        if is_valid_choice(board, mapper, choice):
            break
    row, column = mapper[int(choice)]
    board[row][column] = current_sign
    render_board(board)
    if is_win(board, current_sign):
        print(f"{current_player} won!")
        break
    if is_draw(board):
        print("Game is draw!")
        break
    turn += 1
