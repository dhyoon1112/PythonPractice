
x = int(input("Enter a number: "))
y = range(1,99)

for i in y:
    if x % i == 0:
        print(i)
