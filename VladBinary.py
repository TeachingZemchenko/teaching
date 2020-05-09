from random import randint
spis=[123,234,345,456,567,678,789,890,900,1022]
print(spis)
key=int(input('Введите число для поиска: '))
N=right=len(spis)
left=0
while True:
    b=left+((right-left)//2)
    print('b='+str(b))
    val=spis[b]
    print('val='+str(val))
    print('left='+str(left)+' right='+str(right)+'\n')
    if (b in [0,(N-1)]):
        break
    elif (key==val):
        break
    elif (key>val):
        left=b
    else:
        right=b
if (key==val):
    print('Найдено. Индекс: '+str(b))
else:
    print('Увы, такого значения нет')

    
