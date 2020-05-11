#spis=[-9,-7,0,3,4,9]
#key=-6
b = len(spis) // 2
left = 0
right = len(spis) - 1
while spis[b] != key and left <= right:
    if key > spis[b]:
        left = b + 1
    else:
        right = b - 1
    b = (left + right) // 2
if (b<0):
    b=0
if left > right:
    print("Увы, не найдено. Индекс= ", b) 
else:
    print("Найдено. Индекс=", b)


