def fizzbuzz(a):
    if a % 3 == 0 and a % 5 == 0:
        return 'FizzBuzz'
    if a % 3 == 0:
        return 'fizz'
    if a % 5 == 0:
        return 'buzz'
    return a


b = fizzbuzz(int(input('Digite um número: ')))
print(b)

from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(aleatorio, fizzbuzz(aleatorio))
