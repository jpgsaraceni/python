cont1 = 0
cont2 = 10
while cont1 < 9:
    print(cont1, cont2)
    cont1 += 1
    cont2 -= 1

print('*'*10)

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
