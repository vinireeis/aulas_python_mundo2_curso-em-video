'''Tabuada'''

n = 0

while n >= 0:
    print('-' * 60)
    n = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 60)
    if n >= 0:
        for r in range(1, 11):
            print(f'{n} x {r} = {n * r}')
    else:
        break
print('FIM')
