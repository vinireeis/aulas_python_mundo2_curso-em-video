n = 0
lista = []
result = 0

while n != 999:
    n = int(input("Digite um novo número [999 encerrar]: "))
    if n != 999:
        lista.append(n)
    else:
        break
for i in lista:
    result += i
print(f'foram digitados {len(lista)} números e a soma total é {result}')
