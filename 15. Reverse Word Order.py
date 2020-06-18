def splitwords(n):
    splitwords = n.split()
    return splitwords

words = input("Enter a list of words: ")
print(splitwords(words)[::-1])
