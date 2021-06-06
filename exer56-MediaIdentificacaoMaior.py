'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final
do programa, mostre:
- A média de idade do grupo
- Qual o nome do homem mais velho
- Quantas mulheres têm menos de 20 anos'''


class Pessoa:
    def __init__(self, nome, sexo, idade):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade


pessoas = []
for r in range(4):
    x = input('Informe o nome da pessoa: ')
    y = input('Informe o sexo M/F: ').upper()
    z = int(input('Informe a idade: '))
    a = Pessoa(f'{x}', f'{y}', z)
    pessoas.append(a)

y = 0
x = 0
for r in pessoas:
    x += r.idade
    if r.sexo == 'F':
        y += 1
media = x / len(pessoas)

maioridade = ''
for r in pessoas:
    if r.sexo == 'M':
        if z < r.idade:
            z = r.idade
            maioridade = r.nome
print('-=' * 60)
print(f'A média de idade é {media}')
print(f'A quantidade de pessoas do sexo feminino é: {y}')
print(f'O nome do homem mais velho é {maioridade}')
print('-=' * 60)
