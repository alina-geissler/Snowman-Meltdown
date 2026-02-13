import random

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []
    print("Welcome to Snowman Meltdown!")
    # For now, show the initial game state
    display_game_state(mistakes, secret_word, guessed_letters)
    # For now, get the user input for one first guess
    guess = input("\nGuess a letter: ").lower()
    print("You guessed:", guess)
    guessed_letters.append(guess)


def display_game_state(mistakes, secret_word, guessed_letters):
    # Show the state of the snowman (depending on the number of mistakes)
    print(STAGES[mistakes])
    # Create the version of the secret word to be displayed
    # (using placeholders for letters that have not yet been guessed)
    guessed_so_far = [char if char in guessed_letters else "_" for char in secret_word]
    print(f"(Secret word: {secret_word})")
    print("Word: ", "  ".join(guessed_so_far))


if __name__ == "__main__":
    play_game()
