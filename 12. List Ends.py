import random

def list_generator():
    a = [(random.randint(0,100)) for i in range(random.randint(2,50))]
    return a

x = list_generator()
print(x)

cnt = len(x) - 1
alpha_omega_list = [x[0],x[cnt]]

print(alpha_omega_list)
