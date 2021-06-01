'''Tabuada'''

n = 0
x = int(input('Digite um número para ver sua tabuada: '))
for r in range(1, 11):
    n += 1
    print(f'{x} x {n} = {x * n}')

# Segunda forma de fazer
x = int(input('Digite um número para ver sua tabuada: '))
for r in range(1, 11):
    print(f'{x} x {r} = {x * r}')
