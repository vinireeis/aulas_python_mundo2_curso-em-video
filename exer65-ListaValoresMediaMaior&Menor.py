from statistics import mean

r = 'S'
lista = []
while r == 'S':
  x = int(input('Digite um número: '))
  lista.append(x)
  r = input('Deseja digitar um novo valor? [S/N]').upper
  if r == "N":
    media = mean(lista)
  if r == "S":
    x = int(input('Digite um número: '))
    lista.append(x)
  else:
    r = str(input('Digite uma resposta válida para continuar "s" para Sim e "n" para Não [S/N]:')).upper

print(f'A média dos valores digitados é {media},já o maior valor é {max(lista)} e o menor {min(lista)}')

# while resp != 'N':
#   resp = str(input('Deseja digitar um valor? [S/N]')).upper
#   if resp == 'S':
#     x = int(input("Digite um número: "))
#     lista.append(x)
#   elif resp == 'N':
#     media = mean(lista)
#   else:
#     resp = str(input('Digite uma resposta válida para continuar "s" para Sim e "n" para Não [S/N]:')).upper
# print(f'A média dos valores digitados é {media},já o maior valor é {max(lista)} e o menor {min(lista)}')