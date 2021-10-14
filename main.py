def sub(string, index, newc):
    position = index
    new_character = newc

    string = string[:position] + new_character + string[position + 1:]
    return string  # function for replacing index in string


dc = {}
word = 'youwillnevergetthisright'.replace(' ', '') 
empty = len(word) * '_'
tries = 8   # number of tries
print(empty + ' - letter count is ' + str(len(word)))

while True:  # loop
    user_input = input('\n')
    if user_input.replace(' ', '') == word:
        print('you guessed the word')
        print(word)
        break
    elif user_input in word:
        for i, j in enumerate(word):
            if j == user_input:
                dc[i] = j   # get index of letter in word and storing it in dictionary
        for i in dc.keys():
            empty = sub(empty, i, dc[i])  # the underscore(s) with the letter
        print(f'{empty} - letter count is {empty.count("_")}')
    elif user_input not in word:
        print(f'{user_input} is not in word')
        tries -= 1
    if '_' not in empty:
        print('you guessed the word')
        break
    if tries == 0:
        print('lost')
        break
