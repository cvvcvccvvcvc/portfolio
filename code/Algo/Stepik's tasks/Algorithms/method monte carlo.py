import random

n = 10**6       # количество испытаний
k = 0
for i in range(n):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 <= 1:
        k += 1

print(k/n*4)

