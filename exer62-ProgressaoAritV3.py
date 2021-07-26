print('-' * 60)
print('Gerador de PA')
print('-' * 60)
primeiro = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Fim do programa, foram apresentados {total} termos')
