'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programava vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou o empréstimo será negado'''

casa = int(input('Digite o valor da casa? '))
sal = float(input('Informe o seu salário: '))
anos = float(input('Em quantos anos deseja pagar? '))

r = casa / (anos * 12)
print('-' * 60)
if r > (sal * 0.30):
    print('Empréstimo negado por comprometimento de renda')
else:
    print(f'O valor da sua mensailidade de financiamento será de: {r:.2f}')
print('-' * 60)