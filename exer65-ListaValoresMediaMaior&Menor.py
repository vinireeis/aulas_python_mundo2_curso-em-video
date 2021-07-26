from statistics import mean

r = 'S'
lista = []
while r != 'N':
    r = str(input('Deseja digitar um valor? [S/N]')).upper()
    if r == 'S':
        x = int(input("Digite um número: "))
        lista.append(x)
    elif r == 'N':
        media = mean(lista)
    else:
        r = str(input(
            'Digite uma resposta válida para continuar "s" para Sim e "n" para'
            'Não [S/N]:')).upper()
print(
    f'A média dos valores digitados é {media:.2f}, já o maior valor é '
    f'{max(lista)} e o menor {min(lista)}.')
