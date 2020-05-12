def bubble(spis):
    for i in range(len(spis)):
        for i in range(len(spis) - 1):
            if spis[i] > spis[i + 1]:
                spis[i], spis[i + 1] = spis[i + 1], spis[i]
    return spis
def binary(spis, key):
    b = len(spis) // 2
    left = 0
    right = len(spis) - 1
    while spis[b] != key and left <= right:
        if key > spis[b]:
            left = b + 1
        else:
            right = b - 1
        b = (left + right) // 2
    if (b < 0):
        b = 0
    if left > right:
        return [False, b]
    else:
        return [True, b]
def insert(spis):
    spis1 = []
    g = spis[0]
    spis1.append(g)
    for i in range(1, len(spis)):
        c = spis[i]
        for k in range(len(spis1)):
            if c > spis1[k]:
                if k == (len(spis1) - 1):
                    spis1.append(c)

                continue
            else:
                spisleft = spis1[:k]
                spisleft.append(c)
                spisleft = spisleft + spis1[k:]
                spis1 = spisleft
                break
    return spis1
if __name__ == '__main__':
    print('ты запустил модуль в виде скрипта, так нельзя, подключи его как внешний файл')
    
