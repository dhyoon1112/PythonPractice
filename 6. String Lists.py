user = input("Enter a word: ")
resu = user[::-1]

while user != resu:
    user = input("Enter another word: ")
    resu = user[::-1]
    
    if user == resu:
        print("Your word is a palindrome!: " + resu)
