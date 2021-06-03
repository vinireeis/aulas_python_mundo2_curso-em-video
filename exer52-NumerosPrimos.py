''' Leia um número inteiro e diga se ele é ou não um número primo'''
x = int(input('Digite um número: '))
t = 0
for r in range(1, x+1):
    if x % r == 0:
        t += 1
if t == 2:
    print('Este número é primo')
else:
    print('Este número não é primo')
