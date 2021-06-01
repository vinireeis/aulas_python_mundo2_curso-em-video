''' Faça um programa que leia o ano de nascimento de um jovem e informe de
acordo com a sua idade:
- se ele ainda vai se alistar ao serviço militar
- se é a hora de se alistar
- sejá passou do tempo do alistamento
O programa também deverá mostrar o tempo faltante ou que passou do prazo'''

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
if idade <= 17:
    x = 18 - idade
    print(f'Você ainda vai se alistar, faltam {x} anos.')
elif idade == 18:
    print('Este é o seu ano de alistamento, se atente as datas!')
else:
    x = idade - 18
    print(f'O seu alistamento já passou, foi há {x} anos.')
print('-' * 60)