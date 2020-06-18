import random
import string

password = []
characters = [0,1,2,3,4,5,6,7,8,9]
letters = [string.ascii_letters[i:i+1] for i in range(0, len(string.ascii_letters), 1)]

for i in range(52):
    characters.append(letters[i])

choice = input("Do you want a weak or strong password? (Strong or Weak): ")

while 1==1:
    if choice == "Strong":
        for i in range(random.randint(7,15)):
            password.append(random.choice(letters))
        break
    elif choice == "Weak":
        password = random.choice(["choice","test","random"])
        break
    else:
        "Try again"
        choice = input("Do you want a weak or strong password? (Strong or Weak) ")
    
print(''.join(password))
