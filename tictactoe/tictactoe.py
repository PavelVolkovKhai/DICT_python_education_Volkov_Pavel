cells = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]


def print_board():
    print("---------")
    print("|", cells[0], cells[1], cells[2], "|")
    print("|", cells[3], cells[4], cells[5], "|")
    print("|", cells[6], cells[7], cells[8], "|")
    print("---------")


def check_game_state():
    winning_lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for line in winning_lines:
        if cells[line[0]] == cells[line[1]] == cells[line[2]] == "X":
            return "X wins"

        if cells[line[0]] == cells[line[1]] == cells[line[2]] == "0":
            return "0 wins"

    if "_" not in cells:
        return "Draw"

    return "Game not finished"


current_player = "X"

print_board()

while True:
    coordinates = input("Enter the coordinates:\n").split()

    if len(coordinates) != 2:
        print("You should enter numbers!")
        continue

    if not all(coordinate.isdigit() for coordinate in coordinates):
        print("You should enter numbers!")
        continue

    row = int(coordinates[0])
    column = int(coordinates[1])

    if row < 1 or row > 3 or column < 1 or column > 3:
        print("Coordinates should be from 1 to 3!")
        continue

    index = (row - 1) * 3 + (column - 1)

    if cells[index] != "_":
        print("This cell is occupied! Choose another one!")
        continue

    cells[index] = current_player

    print_board()

    game_state = check_game_state()

    if game_state != "Game not finished":
        print(game_state)
        break

    if current_player == "X":
        current_player = "0"
    else:
        current_player = "X"