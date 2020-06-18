import random

def CowsBulls():
    number = [str(random.randint(0,9)),str(random.randint(0,9)),str(random.randint(0,9)),str(random.randint(0,9))]
    guessarray = []
    count = 0
    #print(number)
    
    while number != guessarray:

        guess = input("Guess a 4 digit number: ")
        guessarray = [digit for digit in guess]
        cows = 0
        bulls = 0
        digit = 0
        count += 1

        for i in guessarray:
            if i == number[digit]:
                cows +=1
                digit +=1
            elif i in number and i != number[digit]:
                bulls +=1
                digit +=1
            else:
                digit +=1
          
        print("Cows: " + str(cows))
        print("Bulls: " + str(bulls))

    print("You won after " + str(count) + " tries!")
    print(number)
            
    return

CowsBulls()
