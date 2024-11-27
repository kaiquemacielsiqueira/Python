soma = 0
qtd = 0
n = int(input('Numero: '))

while n != -1:
    soma +=n
    qtd+=1
    n = int(input('Numero: '))
print(f'Média {soma/qtd}')
