''' A confederação nacional de natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria de acordo com a idade:
- até 9 anos > Mirim
- até 14 anos > Infantil
- até 19 anos > júnior
- até 20 anos > sênior
- acima: Master'''

import datetime

td = datetime.datetime.now().date()
nano = int(input('Digite o ano de seu nascimento: '))
nmes = int(input('Informe o mês: '))
ndia = int(input('Informe o dia: '))
bd = datetime.date(nano, nmes, ndia)
idade = int((td-bd).days / 365.25)
print('-' * 60)
print(f'Você tem {idade} anos.')
print('-' * 60)
if idade <= 9:
    print('Sua categoria é Mirim.')
elif idade <= 14:
    print('Sua categoria é Infantil.')
elif idade <= 19:
    print('Sua categoria é Júnior.')
elif idade <= 25:
    print('Sua categoria é Sênior.')
else:
    print('Sua categoria é Master.')
