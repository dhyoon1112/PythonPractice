import random as r

print("Guess a number between 1 through 10. Type exit if you want to leave")

count = 0
guess = "x"
number = r.randint(1,10)

while guess != number and guess != "exit":
    
    guess = input("Guess a number between 1 through 10: ")
    count += 1

    if guess == "exit":
        print("You quit after " + str(count) + " tries.")
        break

    guess = int(guess)
    
    if guess < number:
        print("You guessed too low")
    elif guess > number:
        print("You guessed too high")
    elif guess == number:
        print("You guess correctly! It took you " + str(count) + " tries.")
