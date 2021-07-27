class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


print('-=' * 20)
print('           CADASTRAR PRODUTOS    ')
print('-=' * 20)
produtos = []

while True:
    n = input('Informe o nome do produto: ')
    p = float(input('Informe o preço do produto: '))
    produto = Produto(f'{n}', p)
    produtos.append(produto)

    x = input('Deseja cadastrar outro produto? [S/N]: ').strip()
    if x in 'Nn':
        break
    elif x in 'Ss':
        print('\nVamos recomeçar..\n')
    else:
        print('Informações inválidas, tente novamente')

maiores = 0
barato = ''
total = 0

for r in produtos:
    total += r.preco
    if p >= r.preco:
        p = r.preco
        barato = r.nome
for r in produtos:
    if r.preco > 1000:
        maiores += 1

print('-=' * 60)
print(f'O valor total das compras é de {total:.2f}\nDe {len(produtos)}'
      f' produtos, {maiores} tem valor maior que R$1000,00\nO produto '
      f'mais barato é o(a) {barato}')

print('-=' * 60)
