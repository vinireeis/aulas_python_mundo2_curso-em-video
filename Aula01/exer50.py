'''Leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor for ímpar desconsidere-o'''

soma = 0
for r in range(1, 6+1):
    x = int(input('Informe um valor: '))
    if x % 2 == 0:
        soma += x
print(soma)


'''
lista = []
soma = 0
for n in lista:
    for r in range(1, 6+1):
    x = int(input('Informe um valor: '))
    if x % 2 == 0:
        lista.append(x)
for n in lista:
    soma += n
print(soma)'''
