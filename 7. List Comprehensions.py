a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [i for i in a if a.index(i) % 2 == 0 and a.index(i) != 0]

print(b)
