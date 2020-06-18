num1 = float(input("Enter two digits for x / y. What is x? "))
num2 = float(input("What is y? "))

result = num1 / num2

if num1 % num2 == 0:
    print("x is a multiple of y and your quotient is: " + str(result))

elif num1 % num2 == 4:
    print("CONTRAGULATIONS YOU ENTERED A MULTIPLE OF 4")

elif num1 % num2 != 1:
    print("x is not a multiple of y and your quotient is: " + str(result))

else:
    print("Invalid entry")
