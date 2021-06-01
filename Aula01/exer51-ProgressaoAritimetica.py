''' Leia um número inteiro e uma razão e diga se ele é uma PA e mostre
os 10 primeiros termos'''

x = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = x + (10 - 1) * r
for i in range(x, d+r, r):
    print(f'{i}', end=' -> ')