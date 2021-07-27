n = 0
lista = []

while n != 999:
    n = int(input("Digite um novo número ou digite 999 encerrar: "))
    if n != 999:
        lista.append(n)
    else:
        break
print(f'foram digitados {len(lista)} números e a soma total é {sum(lista)}')
