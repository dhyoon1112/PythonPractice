import random as r

x = int(input("Enter a number: "))

start = 0
end = 100

a = [1,2,3,4,5,6,7,8,9,10]
b = [r.randint(start,end),r.randint(start,end),r.randint(start,end),r.randint(start,end),r.randint(start,end),r.randint(start,end),r.randint(start,end),r.randint(start,end),r.randint(start,end),r.randint(start,end)]

#for i in b:
#    if i < x:
#        print(i)

for i in b:
    if i < x:
        print(i)
