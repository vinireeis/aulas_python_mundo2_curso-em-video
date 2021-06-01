''' Jogo pedra papel e tesoura'''
from random import randint
print('-' * 60)
jogo = ['Pedra', 'Papel', 'Tesoura']
x = int(input('Escolha uma opção para jogar:\n0 - Pedra\n1 - Papel\n2- Tesoura'
              '\n'))
ia = randint(0, 2)
print('-' * 60)
print(f'A IA escolheu {jogo[ia]}.')
print(f'Você escolheu {jogo[x]}.')
print('-' * 60)

if ia == 0 and x == 0:
    print(f'O jogo empatou, os dois jogaram {jogo[0]}')
elif ia == 0 and x == 1:
    print('Parabéns você ganhou!')
elif ia == 0 and x == 2:
    print('Você perdeu')
elif ia == 1 and x == 0:
    print('Você perdeu')
elif ia == 1 and x == 1:
    print(f'O jogo empatou, os dois jogaram {jogo[1]}')
elif ia == 1 and x == 2:
    print('Parabéns você ganhou!')
elif ia == 2 and x == 0:
    print('Parabéns você ganhou!')
elif ia == 2 and x == 1:
    print('Você perdeu')
elif ia == 2 and x == 2:
    print(f'O jogo empatou, os dois jogaram {jogo[2]}')
else:
    print('Opção inválida')
print('-' * 60)
