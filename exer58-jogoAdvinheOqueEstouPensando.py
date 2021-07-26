''' escreva um programa que faça o computador "pensar" em um número inteiro
    entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
    escolhido pelo computador'''
import random

n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sort = random.choice(n)
print('-' * 60)
cont = 0
n1 = int(input('O computador está pensando em um número de 0 a 10, digite um'
               ' número e veja se você adivinha o mesmo valor: '))
print('-' * 60)
while sort != n1:
    n1 = int(input('Você errou, tente novamente digitando'
                   ' um novo número: '))
    cont += 1
    print('-' * 60)
print(f'Parabéns o computador pensou no {sort}, sendo'
      f' que você precisou de {cont} tentativas para acertar.')
