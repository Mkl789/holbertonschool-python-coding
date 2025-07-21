#!/usr/bin/python3
import random
def get_random_word():
    with open('wordlist.txt', 'r') as file:
        text = file.read()
    words = text.split()
    random_word = random.choice(words)
    print(random_word)
get_random_word()
