x = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = x + (10 - 1) * r
for i in range(x, d+r, r):
    print(f'{i}', end=' -> ')
print('Acabou!')
