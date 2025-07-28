#!/usr/bin/python3
class HangmanGame:
    def __init__(self, word, guessed_letters, max_errors, errors=0):
        self.word = word #(the target word)
        self.guessed_letters = guessed_letters #(letters the user has guessed)
        self.max_errors = max_errors #(set to 6)
        self.errors = errors #(number of wrong guesses)    
    def display_progress(self):
        for letter in self.word:
            if not letter.isalpha():
                print(letter, end=" ")
            elif letter in self.guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print() # move to the next line
    def process_guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters:  
            self.guessed_letters.append(letter)
            print("Correct Guess")
        else:
            self.errors += 1
            print("Wrong Guess")
    def is_lost(self):
        return self.errors >= self.max_errors
    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.word)
        