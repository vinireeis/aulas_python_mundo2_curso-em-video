''' Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar
qual tipo de triângulo será formado:
- equilátero: todos os lados iguais
- isósceles: dois lados iguais
- escaleno: todos os lados diferentes'''

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
t1 = float(input('Informe o tamanho do primeiro seguimento: '))
t2 = float(input('Informe o segundo seguimento: '))
t3 = float(input('Informe o terceiro seguimento: '))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os seguimentos digitados, podem formar um triângulo!')
    if t1 != t2 != t3 != t1:
        print('Este é um triângulo ESCALENO')
    elif t1 == t2 == t3:
        print("Este é um triângulo EQUILÁTERO!")
    else:
        print('Este é um triângulo ISÓSCELES')
else:
    print('Os seguimentos não podem formar um triângulo!')
