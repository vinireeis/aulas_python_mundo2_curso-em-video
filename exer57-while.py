sexo = input('Informe o seu sexo [M/F]: ').upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Informe corretamente o seu sexo [M/F]: ').upper()
if sexo == 'M':
    print('-' * 30)
    print('Você é do sexo Masculino')
elif sexo == 'F':
    print('-' * 30)
    print('Você é do sexo Feminino')

# sexo = input('Informe o seu sexo [M/F]: ').strip().upper()
# while sexo not in 'MmFf':
#     sexo = input('Informe corretamente o seu sexo [M/F]: ').strip().upper()
# print(f'Sexo {sexo} registrado com sucesso')