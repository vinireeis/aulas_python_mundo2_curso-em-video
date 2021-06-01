'''faça um programa que mostre uma contagem regressiva de 10 até 0 para o
estouro de fogos com pausa de 1 segundo entre as contagens'''
from time import sleep

print('Contagem regressiva para os fogos de artifício já vai começar!')
for r in range(10, -1, -1):
    print(r)
    sleep(0.7)
print('Feliz ano novo!!!')
