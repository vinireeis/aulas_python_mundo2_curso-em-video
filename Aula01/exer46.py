'''faça um programa que mostre uma contagem regressiva de 10 até 0 para o
estouro de fogos com pausa de 1 segundo entre as contagens'''
import time

print('Contagem regressiva para os fogos de artifício já vai começar!')
for r in range(10, 0, -1):
    print(r)
    time.sleep(1.0)
print('Feliz ano novo!!!')
