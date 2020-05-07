from random import randint
N = int(input('vvedite n'))
spis = [randint(-100, 100) for i in range(N)]
print(spis)
for i in range(N):
    for i in range(len(spis) - 1):
        if spis[i] > spis[i + 1]:
            spis[i], spis[i + 1] = spis[i + 1], spis[i]
print(spis)





