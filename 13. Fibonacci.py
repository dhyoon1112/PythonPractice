def fibonacci(n):
    a = []
    for i in range(n):
        if i <= 1:
            a.append(1)
        else:
            a.append(a[i-1]+a[i-2])
    return a


number = input("How many fibonacci numbers do you want? ")
print(fibonacci(int(number)))
