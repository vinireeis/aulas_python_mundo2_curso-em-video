'''Escreva um programa que leia dois números inteiros
e compare-os, mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior, os dois são iguais'''

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
if x > y:
    print('O primeiro valor é o maior número')
elif y > x:
    print('O segundo valor é o maior número')
else:
    print('Os dois valores são equivalentes')
