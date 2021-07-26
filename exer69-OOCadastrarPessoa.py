''' Ler idade e sexo, perguntar se quer cadastrar outra pessoa ou não
No fim, mostre:
    Quantas pessoas > 18 anos.
    Quantos homens
    Quantas mulheres < 20 anos'''


class Pessoa:
    def __init__(self, idade, sexo):
        self.idade = idade
        self.sexo = sexo


pessoas = []
print('-=' * 20)
print('     CADASTRE UMA PESSOA     ')
print('-=' * 20)
while True:
    s = input('Informe o sexo [M/F]: ').strip()
    i = int(input('Informe a idade: '))
    if s in 'MmFf' and i >= 0:
        pessoa = Pessoa(i, f'{s}')
        pessoas.append(pessoa)
        x = input('Deseja continuar? [S/N]: ').strip()
        if x in 'Nn':
            break
        elif x in 'Ss':
            print('\nVamos para próxima pessoa!\n')
        else:
            print('Informações inválidas, digite novamente')
    else:
        print('Informações inválidas, digite novamente')


maiores = 0
homens = 0
mulheres = 0
for r in pessoas:
    if r.idade > 18:
        maiores += 1
        if r.sexo in 'Mm':
            homens += 1
    elif r.sexo in 'Mm':
        homens += 1
    elif r.sexo in 'Ff' and r.idade < 20:
        mulheres += 1


print(f'\nO total de maiores de 18 anos é {maiores}.\nO total de homens é'
      f' {homens}.'
      f'\nO total de mulheres com idade menor a 20 anos é {mulheres}.')
