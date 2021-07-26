n = int(input("Informe um número para descobrir o seu fatorial: "))
cont = n - 1

while cont > 0:
    n = n * cont
    cont -= 1
print(f'O fatorial é {n}')


# from math import factorial
# n = int(input("Digite um numero para calcular o fatorial: "))
# f = factorial(n)
# print(f'O fatorial de {n} é {f}.')
