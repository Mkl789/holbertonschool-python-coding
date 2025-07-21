#!/usr/bin/python3
class HangmanGame:
    def __init__(self, word, guessed_letters, max_errors, errors):
        self.word = word #(the target word)
        self.guessed_letters = guessed_letters #(letters the user has guessed)
        self.max_errors = max_errors #(set to 6)
        self.errors = errors #(number of wrong guesses)    
    def display_progress(self):
        for letter in self.word:
            if letter in self.guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print() # move to the next line
