from game import HangmanGame
from utils import get_random_word

while True:
    word = get_random_word()
    game = HangmanGame(word=word, guessed_letters=[], max_errors=6)
    previous_inputs = set()

    while True:
        user_input = input("Please enter a letter: ")
        if not (user_input.isalpha() and len(user_input) == 1):
            input("Invalid input. Press enter to try again.")
            continue
        if user_input in previous_inputs:
            print("This letter has already been entered.")
        else:
            previous_inputs.add(user_input)
            print(f"You entered: {user_input}")
            game.process_guess(user_input)
            game.display_progress()
            print("Guessed letters:", ' '.join(game.guessed_letters))
            print(f"Tries remaining: {game.max_errors - game.errors}")

        if game.is_won():
            print("You won!")
            break
            
        elif game.is_lost():
            print(f"Game over! The word was: {game.word}")
            break
    retry = input("Play again? (yes/no): ").strip().lower() 
    if retry != 'yes':                                       
        print("Alright, Thanks for playing! (That was way to many lines of code for such a simple game)")                
        break  