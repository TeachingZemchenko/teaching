
from random import randint
mass = []
for i in range (100):
    mass.append(i)
key = int(input('  vvedite chislo key'))

#mass = [112, 123, 321, 454, 556, 643, 864, 976, 999, 1001]
print(mass)
n =len(mass)
g = int((n / 2))
b = mass[g]
gpet = n -1
while b != key:

    if key < b:
        gpet = g - 1
        g = g // 2
        b = mass[g]
        if g == 0:
            break
    else:
        g = int(((gpet-g) / 2) + g)
        b = mass[g]
        if g == (n - 1):
            break


if key == b:
    print('ind = ' + str(g) + '    ' + str(b))
else:
    print('element dosen\'t found')




