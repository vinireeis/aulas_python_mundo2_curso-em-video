''' Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem de acordo com a média atingida:
- média abaixo de 5.0 : reprovado
- média entre 5.0 e 6.9: recuperação
- média 7.0 ou superior: aprovado
'''

x = float(input('Informe a primeira nota: '))
y = float(input('Informe a segunda nota: '))
r = (x + y) / 2
if r < 5.0:
    print('-' * 60)
    print('Você está reprovado')
elif r > 4.9 and r < 6.9:
    print('-' * 60)
    print('Você está de recuperação')
else:
    print('-' * 60)
    print('Você está aprovado!')
print('-' * 60)
print(f'Sua média é: {r}')
print('-' * 60)
