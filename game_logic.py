import random

from snowman_words import WORDS
from ascii_art import STAGES


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        if mistakes < 3:
            guess = input("\nGuess a letter: ").lower()
            guessed_letters.append(guess)
            if guess not in secret_word:
                mistakes += 1
        elif mistakes == 3:
            break


def display_game_state(mistakes, secret_word, guessed_letters):
    if mistakes == 3:
        print(f"Game over! The word was: {secret_word}")
        print(STAGES[mistakes])
        return
    guessed_so_far = [char if char in guessed_letters else "_" for char in secret_word]
    if "_" in guessed_so_far:
        print(STAGES[mistakes])
        print("Word: ", "  ".join(guessed_so_far))
        return False
    else:
        print("Congratulations, you saved the snowman!")
        exit()


def main():
    print("Welcome to Snowman Meltdown!")
    play_game()


if __name__ == "__main__":
    main()
