''' Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços'''

frase = str(input('Digite um frase: ')).strip().upper()
p = frase.split()
print(p)
j = ''.join(p)
inverso = ''
for letra in range(len(j) - 1, -1, -1):
    inverso += j[letra]
if inverso == j:
    print('Essa string é um palíndromo')
else:
    print('Não é um palíndromo')
