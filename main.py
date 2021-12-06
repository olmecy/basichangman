import random
import time
from words import words
def sub(string, index, newc):
    position = index
    new_character = newc

    string = string[:position] + new_character + string[position + 1:]
    return string  # function for replacing index in string


dc = {}
word = random.choice(words)
empty = len(word) * '_'
tries = 15   # number of tries
guessedletters = []
print(empty + ' - letter count is ' + str(len(word)))

while True:  # loop
    user_input = input('\n')
    # Checking if user guessed word right
    if user_input == word:
        print('you guessed the word')
        print(word)
        time.sleep(5)
        break

    # Checking if one of users letters in word

    elif user_input in word:
        # Adding letter to guessedletter and checking if it's guessed
        guessedletters.append(user_input)
        if user_input in guessedletters:
            print('you already guessed this')
        for i, j in enumerate(word):
            if j == user_input:
                dc[i] = j   # get index of letter in word and storing it in dictionary
        for i in dc.keys():
            empty = sub(empty, i, dc[i])  # the underscore(s) with the letter
        print(f'{empty} - letter count is {empty.count("_")}')
        dc.clear()

    elif user_input not in word:
        if user_input in guessedletters:
            print('you already guessed this (it\'s wrong)')
        else:
            print(f'{user_input} is not in word')
            guessedletters.append(user_input)
            tries -= 1
        print(f'{empty} - letter count is {empty.count("_")}')

    # check if word is completed
    if '_' not in empty:
        print('you guessed the word')
        break
    if tries == 0:
        print('lost')
        time.sleep(5)
        break
