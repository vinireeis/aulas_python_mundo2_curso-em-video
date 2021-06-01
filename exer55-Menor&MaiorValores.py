''' Faça um programa que leia o peso de 5 pessoas e diga qual foi o maior
 e menor pesos lidos'''

pesos = []
for r in range(1, 5+1):
    x = float(input('Informe o próximo peso: '))
    pesos.append(x)
print(max(pesos))
print(min(pesos))
