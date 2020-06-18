import random as rand

list1 = []
list2 = []
for i in range(0,10):
    list1.append(rand.randint(1,30))
    list2.append(rand.randint(1,30))

for i in list1:
    if i in list2:
        print(i)
                         
