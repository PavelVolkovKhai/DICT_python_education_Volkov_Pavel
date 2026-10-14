import random


def play_hangman():
    words = ["python", "java", "javascript", "php"]
    secret_word = random.choice(words)
    guessed_letters = set()
    lives = 8

    while True:
        current_state = "".join(
            letter if letter in guessed_letters else "-"
            for letter in secret_word
        )

        print(current_state)

        if current_state == secret_word:
            print(f"You guessed the word {secret_word}!")
            print("You survived!")
            return

        if lives == 0:
            print("You lost!")
            return

        guess = input("Input a letter: > ")

        if len(guess) != 1:
            print("You should input a single letter")
            continue

        if not ("a" <= guess <= "z"):
            print("Please enter a lowercase English letter")
            continue

        if guess in guessed_letters:
            print("You've already guessed this letter")
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            print("That letter doesn't appear in the word")
            lives -= 1

            if lives == 0:
                current_state = "".join(
                    letter if letter in guessed_letters else "-"
                    for letter in secret_word
                )
                print(current_state)
                print("You lost!")
                return


def main():
    print("HANGMAN")

    while True:
        choice = input(
            'Type "play" to play the game, "exit" to quit: > '
        )

        if choice == "play":
            play_hangman()
        elif choice == "exit":
            break


if __name__ == "__main__":
    main()