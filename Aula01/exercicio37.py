'''Escreva um programa que leia um número inteiro qualquer e peça para o
usuário escolher qual será a base de conversão: 1 para binário 2 para octal
 3 para hexadecimal'''

n = int(input('Digite um número inteiro para ser convertido: '))
r = int(input('Escolha uma das seguintes opções de conversão:\n1 - para'
              ' binário\n2 - para octal\n3 - para hexadecimal\n '))

if r == 1:
    n = bin(n)
    print(n)
elif r == 2:
    n = oct(n)
    print(n)
elif r == 3:
    n = hex(n)
    print(n)
else:
    print('Opção inválida.')
