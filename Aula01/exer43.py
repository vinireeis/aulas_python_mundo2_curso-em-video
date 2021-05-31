'''Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu
IMC e mostre seu status, de acordo com a tabela abaixo:
- abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida'''

a = float(input('Informe sua altura: '))
p = float(input('Informe o seu peso: '))

imc = p / (a * a)

if imc < 18.5:
    print('Abaixo do peso atual')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
elif imc > 40.0:
    print('Obesidade Mórbida')
print('-' * 60)
print(f'{imc:.1f}')
print('-' * 60)
