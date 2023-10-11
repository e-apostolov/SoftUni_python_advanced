ROWS = 6
COLUMNS = 7

direction_mapper = {
    "up": (-1, 0),
    "right": (0, 1),
    "left_up": (-1, -1),
    "right_up": (-1, 1),
}


class FullColumnError(Exception):
    pass


def print_field(field):
    for row in game_field:
        print(row)


def is_valid_column_choice(column_index):
    if 0 <= column_index < COLUMNS:
        return True
    return False


def place_player_number(column_index, field, player_number):
    for row_index in range(ROWS-1, -1, -1):
        if field[row_index][column_index] == 0:
            field[row_index][column_index] = player_number
            return row_index, column_index
    else:
        raise FullColumnError


def requested_direction_count(row, column, coordinates, field, player_number):
    count = 1
    for i in range(1, 4):
        if 0 <= row + coordinates[0] * i < ROWS and 0 <= column + coordinates[1] * i < COLUMNS:
            row_index_to_check = row + coordinates[0] * i
            column_index_to_check = column + coordinates[1] * i

            if field[row_index_to_check][column_index_to_check] != player_number:
                break
            count += 1
    return count


def opposite_direction_count(row, column, coordinates, field, player_number):
    count = 0
    for i in range(1, 4):
        if 0 <= row - coordinates[0] * i < ROWS and 0 <= column - coordinates[1] * i < COLUMNS:
            row_index_to_check = row - coordinates[0] * i
            column_index_to_check = column - coordinates[1] * i

            if field[row_index_to_check][column_index_to_check] != player_number:
                break
            count += 1
    return count


def is_winner(row, column, field, player_number):
    for direction, coordinates in direction_mapper.items():
        count_direction = requested_direction_count(row, column, coordinates, field, player_number)
        count_opposite_direction = opposite_direction_count(row, column, coordinates, field, player_number)

        if count_direction + count_opposite_direction >= 4:
            return True
    return False


game_field = [[0 for _ in range(COLUMNS)]for row in range(ROWS)]
print_field(game_field)

player = 1

while True:
    try:
        selected_column_index = int(input(f"Player {player}, please choose a column: ")) - 1
        if not is_valid_column_choice(selected_column_index):
            raise ValueError
        current_row, current_column = place_player_number(selected_column_index, game_field, player)
        if is_winner(current_row, current_column, game_field, player):
            print(f"Player {player} wins!")
            print_field(game_field)
            break
        print_field(game_field)
    except ValueError:
        print(f"Player {player}, Please select number between 1 and {COLUMNS}!")
        continue
    except FullColumnError:
        print(f"Player {player}, this column is full, please select another one!")
        continue
    player += 1
    player = 2 if player % 2 == 0 else 1