'''Leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor for ímpar desconsidere-o'''
lista = []
for r in range(1, 6+1):
    x = int(input('Informe um valor: '))
    if x % 2 == 0:
        lista.append(x)
y = 0
for r in lista:
    y += r
print(r)
