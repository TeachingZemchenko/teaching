import time


from random import randint
N = int(input('vvedite n   '))
a = time.time()
spis = [randint(-10, 10) for i in range(N)]
#spis=[-3,-5,-9]
#N=3
print(spis)
spis1 = []
g = spis[0]
spis1.append(g)
for i in range(1, N):
    c = spis[i]
    for k in range(len(spis1)):
        if c > spis1[k]:
            if k == (len(spis1) -1):
                spis1.append(c)

            continue
        else:
            spisleft = spis1[:k]
            spisleft.append(c)
            spisleft = spisleft + spis1[k:]
            spis1 = spisleft
            break

print(spis1)
b = time.time()
print(b - a)










