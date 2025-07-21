#!/usr/bin/python3
import random
with open('wordlist.txt', 'r') as file:
    text = file.read()
words = text.split()
random_word = random.choice(words)
print(random_word)
