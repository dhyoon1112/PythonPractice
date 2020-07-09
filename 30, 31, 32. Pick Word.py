import random

#download the sowpods text file: http://norvig.com/ngrams/sowpods.txt

def read():
    array = []
    with open('30.sowpods.txt','r') as file:
        text = file.readline().strip()
        while len(array) <= 50:
            text = file.readline().strip()
            array.append(text)

    return random.choice(array)
        
word = read()
#print(word)


def guessing(x):

    blanks = ['_' for _ in x]
    word = [_ for _ in x]
    wrongguesses = []

    while len(set(wrongguesses)) < 6:
        
        lettercounter = 0
        guess = input("Guess a letter: ")
        
        for _ in word:

            if guess == blanks[lettercounter]:
                print("You already guessed that letter, try again")
                break
            
            elif _ == guess:
                blanks[lettercounter] = guess

            elif blanks == word:
                print("You win")
                return False

            elif guess not in set(word):
                wrongguesses.append(guess)

            lettercounter += 1

        print("You have " + str(6 - len(set(wrongguesses))) + " guesses left")
        print(' '.join(blanks))



guessing(word)

