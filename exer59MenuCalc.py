n = 4
valor1 = float(input('Informe o primeiro valor: '))
valor2 = float(input('Informe o segundo valor: '))
while n != 5:
    n = int(input(('-' * 60) + '\nEscolha uma das opções abaixo: \n[1]SOMAR'
                  '\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NUMEROS\n[5]SAIR\n' +
                  '-' * 60 + '\n'))
    if n == 1:
        x = valor1 + valor2
        print(f'O resultado da soma é {x}')
    elif n == 2:
        x = valor1 * valor2
        print(f'O resultado da multiplicação é {x}')
    elif n == 3:
        if valor1 > valor2:
            print(f'O maior valor é {valor1}')
        elif valor1 == valor2:
            print('Os dois valores são equivalentes')
        else:
            print(f'O maior valor é {valor2}')
    elif n == 4:
        valor1 = float(input('Informe o primeiro valor: '))
        valor2 = float(input('Informe o segundo valor: '))
    else:
        print('-' * 60)
        print('Digite uma opção correta')
