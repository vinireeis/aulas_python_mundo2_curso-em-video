from random import randint

print("-=" * 30)
print('Vamos jogar PAR ou ÍMPAR')
print("-=" * 30)
vitorias = 0

while True:
    valorj = int(input('Informe um número para jogar: '))
    aposta = str(input('Par ou Ímpar? [P/I]: ')).strip()
    if valorj >= 0 and aposta in "pPiI":
        valorpc = randint(0, 5)
        vencedor = valorj + valorpc
        if aposta in "pP" and vencedor % 2 == 0:
            print(f'\n Você apostou {valorj} o computador apostou {valorpc} e'
                  ' o total foi o número {vencedor}, portando é PAR e você'
                  ' acertou, PARABÉNS!\n Vamos para a próxima rodada! \n')
            vitorias += 1
        elif aposta in "iI" and vencedor % 2 != 0:
            print(f'\n Você apostou {valorj} o computador apostou {valorpc} e'
                  f' o total foi o número {vencedor}, portando é ÍMPAR e você'
                  ' acertou, PARABÉNS! \n Vamos para a próxima rodada! \n')
            vitorias += 1
        else:
            print(f'Você apostou {valorj} e o PC {valorpc} sendo o total'
                  f' {vencedor} ')
            print('\nGAME OVER, o computador ganhou!')
            break
    else:
        print('Foram inseridas informações incorretas, tente novamente!')
print("-=" * 30)
print(f'Você ganhou {vitorias} vez(es), até mais!')
print("-=" * 30)
