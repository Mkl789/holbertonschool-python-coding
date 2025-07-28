#!/usr/bin/python3
import os
import random
def get_random_word():
    with open ('wordlist.txt') as file:
        text = file.read()
    words = text.split()
    random_word = random.choice(words)
    return random_word

#IN CASE THE WORDLIST FIL CAN'T BE FOUND:
# cd "C:\Users\Khatije Lalmahomed\Desktop\holbertonschool-python-coding\holbertonschool-python-coding\hangman_project"
# --> Command to change the directory (select the right one(hangman_project))