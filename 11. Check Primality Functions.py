def prime(n):
    if int(n) % 2 == 0 or int(n) % 3 == 0:
        return print(str(n) + ' is not a Prime Number')
    else:
        return print(str(n) + ' is a Prime Number')

        
number = int(input('Enter a number to see if it is prime: '))
prime(number)
