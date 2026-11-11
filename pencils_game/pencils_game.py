
import random


while True:
    pencils_input = input("How many pencils would you like to use:\n> ")

    if not pencils_input.isdigit():
        print("The number of pencils should be numeric")
        continue

    pencils = int(pencils_input)

    if pencils <= 0:
        print("The number of pencils should be positive")
        continue

    break


players = ["John", "Jack"]

while True:
    first_player = input("Who will be the first (John, Jack):\n> ")

    if first_player not in players:
        print("Choose between 'John' and 'Jack'")
        continue

    break


print("|" * pencils)
print(f"{first_player} is going first!")

current_player = players.index(first_player)

while pencils > 0:
    player = players[current_player]

    print(f"{player}'s turn:")

    if player == "John":
        while True:
            taken = input("> ")

            if taken not in ("1", "2", "3"):
                print("Possible values: '1', '2' or '3'")
                continue

            taken = int(taken)

            if taken > pencils:
                print("Too many pencils were taken")
                continue

            break

    else:
        if pencils % 4 != 1:
            taken = (pencils - 1) % 4
        else:
            taken = random.randint(1, min(3, pencils))

        print(taken)

    pencils -= taken

    if pencils == 0:
        winner = players[1 - current_player]
        print(f"{winner} won!")
        break

    print("|" * pencils)

    current_player = 1 - current_player
