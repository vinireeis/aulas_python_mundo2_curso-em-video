''' Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas são maiores e quantas não.'''

import datetime
maior = 0
menor = 0
for r in range(1, 7+1):
    td = datetime.datetime.now().date()
    nano = int(input('Digite o ano de seu nascimento: '))
    nmes = int(input('Informe o mês: '))
    ndia = int(input('Informe o dia: '))
    bd = datetime.date(nano, nmes, ndia)
    idade = int((td-bd).days / 365.25)
    print('-' * 60)
    print(f'Você tem {idade} anos.')
    print('-' * 60)
    if idade <= 17:
        menor += 1
    else:
        maior += 1
print(f'São {maior} pessoas maiores e {menor} menores de idade.')
print('-' * 60)
