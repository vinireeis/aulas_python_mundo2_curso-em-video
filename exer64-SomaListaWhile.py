n = 0
lista = []
result = 0

while n != 999:
  n = int(input("Digite um novo número: "))
  if n != 999:
    lista.append(n)
  else:
    for i in lista:
      result += i
print(f'foram digitados {len(lista)} números e o resultado é {result}')
