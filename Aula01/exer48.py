'''Faça um programa que calcule a soma entre todos os números ímpares que são
múltiplos de três e que se encontram no intervalo de 1 até 500.'''
x = 0
for r in range(1, 501):
    if r % 2 != 0:
        x += r
print(f'A soma total é {x}.')
