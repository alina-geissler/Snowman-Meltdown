import random
import colorama

from snowman_words import WORDS
from ascii_art import STAGES

colorama.init(autoreset=True)


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []
    print(colorama.Fore.MAGENTA + "\nGuess the secret word before the snowman melts away!")
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        if mistakes < 3:
            guess = get_valid_guess(guessed_letters)
            guessed_letters.append(guess)
            if guess not in secret_word:
                mistakes += 1
                print(colorama.Fore.CYAN + "Oh no! The snowman is melting...")
            else:
                print(colorama.Fore.CYAN + "That's a hit! Your guess prevented the snowman from melting!")
        elif mistakes == 3:
            break


def get_valid_guess(guessed_letters):
    while True:
        guess = input(colorama.Fore.BLUE + "\nGuess a letter: ").lower()
        if len(guess) != 1:
            print(colorama.Fore.RED + "Please enter a single letter!")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print(colorama.Fore.RED + "Please enter a letter!")
        elif guess in guessed_letters:
            print(colorama.Fore.RED + "You already guessed that letter!")
        else:
            return guess


def display_game_state(mistakes, secret_word, guessed_letters):
    print(colorama.Fore.CYAN + STAGES[mistakes])
    if mistakes == 3:
        print(colorama.Fore.MAGENTA + f"\nGame over, the snowman has completely melted!\n"
                                      f"The secret word was: {secret_word}\n")
        play_again = does_user_want_to_play_again()
        if play_again:
            play_game()
        else:
            return
    else:
        guessed_so_far = [char if char in guessed_letters else "_" for char in secret_word]
        if "_" in guessed_so_far:
            print(colorama.Fore.MAGENTA + "Word: ", "  ".join(guessed_so_far))
        else:
            print(colorama.Fore.MAGENTA + f"\nCongratulations, you saved the snowman!\n"
                                          f"You found the secret word: {secret_word}\n")
            play_again = does_user_want_to_play_again()
            if play_again:
                play_game()
            else:
                exit()


def does_user_want_to_play_again():
    while True:
        play_again = input(colorama.Fore.YELLOW + "Do you want to play again? (Y/N) ").upper()
        if play_again not in ("Y", "YES", "N", "NO"):
            print(colorama.Fore.RED + "PLease enter 'Y' or 'N'!")
        elif play_again in ("Y", "YES"):
            return True
        else:
            return False


def main():
    print(colorama.Style.BRIGHT + colorama.Fore.BLUE + "Welcome to Snowman Meltdown!")
    play_game()


if __name__ == "__main__":
    main()
