''' escreva um programa que faça o computador "pensar" em um número inteiro
    entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
    escolhido pelo computador'''
import random
from random import randint
from time import sleep

n = [0, 1, 2, 3, 4, 5]
sort = random.choice(n)
print('-' * 60)
n1 = int(input('O computador está pensando em um número de 0 a 5, digite um'
               ' número para saber se acertou o mesmo valor: '))
print('-' * 60)
while sort != n1:
    print(f'Você errou, o computador pensou no {sort} e você digitou {n1}.')
    n1 = int(input('Tentei novamente digitando um novo número: '))
    sort = random.choice(n)
    print('-' * 60)
if sort == n1:
    print(f'Parabéns o computador pensou no {sort} e você digitou {n1}.')
else:
    print('Você errou, o computador pensou em outro número')
    print(f'eu pensei no {sort} e você digitou {n1}.')

''' forma de resolução do guanabara
comp = randint(0, 5)
print('-=-' * 20)
print('Estou pensando em um número de 0 a 5. Tente adivinhar')
print('-=-' * 20)
n = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(2)
if n == comp:
    print(f'Parabéns eu pensei no número {comp} e você digitou o mesmo {n}')
else:
    print(f'Ganhei! eu pensei no número {comp} e você digitou {n}.')'''
