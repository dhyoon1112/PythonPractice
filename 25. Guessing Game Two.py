import random

def guess2():

    counter = 1
    array = [_ for _ in range(1,101)]
    guesses = [0]
    numbers = []
    start = 0
    end = 100

    while True:
        guess = random.randint(start,end)
        print("Is your number lower or higher than " + str(guess))
        number = input("Type 'higher' or 'lower' or 'correct' : ")
        guesses.append(guess)
        numbers.append(number)

        if number == "higher" and numbers[counter-1] == "lower":
            start = guesses[counter-1] + 1

        elif number == "lower" and numbers[counter-1] == "higher":
            end = guesses[counter-1] - 1

        elif number == "higher":
            start = guess

        elif number == "lower":
            end = guess

        elif number == "correct":
            print("I got it! It's " + str(guess) + " and it took " + str(counter) + " guesses.")
            break

        array = [_ for _ in range(start,end)]
        counter += 1

        '''print(guesses)
        print(numbers)
        print(array)'''



guess2()
