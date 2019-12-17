import time
import sys
try:
    with open(sys.argv[2], encoding='utf-8') as fileObject:   # read letter values
        values_list = [values.replace("I", "ı").replace("İ", "i").lower().split(':') for values in fileObject]
        values_dict = {i[0]: int(i[1]) for i in values_list}


    def score(keys):    # calculate of point of one letter
        sum_of_keys = 0
        for i in keys:
            sum_of_keys += values_dict[i]
        return sum_of_keys*len(keys)


    with open(sys.argv[1], encoding='utf-8') as file:   # read correct word
        letters = [line.replace("I", "ı").replace("İ", "i").lower().split(':') for line in file]
        for words in letters:   # loop for list of shuffled letters
            correct_word = words[1][:-1].split(',')   # list of correct words
            print("Shuffled letters are: ", words[0], " Please guess words for these letters with minimum three letters")
            clock = 30   # we have 30 time
            guessed_list = []
            while True:   # guess letter in each 30 times
                start_time = time.time()
                guess = input("Guessed word: ")
                duration = int(time.time() - start_time)    # elapsed time
                clock -= duration
                if 0 < clock < 30:
                    if guess not in guessed_list:
                        if guess in correct_word:
                            guessed_list.append(guess)
                        else:
                            print("Your guessed word is not a valid word")
                    else:
                        print("This word guessed before")
                    print("You have {} time".format(clock))
                else:
                    break
            total = 0
            for word in guessed_list:
                total += score(word)   # total score for one shuffled letters
            print("Score for {} is {}".format(words[0], total), "and guessed words are: {}".format('-'.join(guessed_list)))
except IndexError:
    print("You must write two arguments for this program")
