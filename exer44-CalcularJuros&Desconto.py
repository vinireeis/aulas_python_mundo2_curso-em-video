'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheir/cheque > 10% de desconto
- à vista no cartão > 5% de desconto
- em até 2x no cartão > preço normal
- 3x ou mais no cartão > 20% de juros'''

p = float(input('Informe o preço do produto: '))
c = int(input('Informe a condição de pagamento:\n1 - à vista dinheiro ou'
              ' cheque\n2 - à vista no cartão\n3 - em até 2x no cartão\n4 - em'
              ' 3x ou mais no cartão\n'))

if c == 1:
    p = p * 0.90
elif c == 2:
    p = p * 0.95
elif c == 4:
    p = p * 1.20
elif c == 3:
    p = p
else:
    print('Opção inválida.')
print(f'O valor a ser pago pelo produto é: R${p:.2f}')
