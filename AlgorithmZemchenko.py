from random import randint
from time import time
N = int(input('vvedite n      '))

spis = [randint(-100, 100) for i in range(N)]
spis1 = list(spis)
a = time()
print(spis)
kol = 0

for k in range(N):
    kol = kol + 1
    for i in range(len(spis) - 1):
        if spis[i] > spis[i + 1]:
            spis[i], spis[i + 1] = spis[i + 1], spis[i]
print(kol)

b = time()
c = b - a
print(c)
print(spis)
d = time()
kol = 0

for k in range(N):
    transposition = False
    kol = kol + 1
    for i in range(len(spis1) - 1):
        if spis1[i] > spis1[i + 1]:
            spis1[i], spis1[i + 1] = spis1[i + 1], spis1[i]
            transposition = True



    if transposition == False:
        break

print(kol)
print(spis1)
g = time()
h = g - d
print(h)

print(c - h)






