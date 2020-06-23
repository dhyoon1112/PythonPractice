one = int(input("Enter 1st number: "))
two = int(input("Enter 2nd number: "))
three = int(input("Enter 3rd number: "))

if one > two and one > three:
    print(one)
elif two > one and two > three:
    print(two)
elif three > one and three > two:
    print(three)
