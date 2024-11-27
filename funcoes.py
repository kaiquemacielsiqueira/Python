def pede_idade(mensagem):
    idade = int(input(mensagem))
    return idade

idade = pede_idade('Digite sua idade: ')

if idade > 18:
    print('De maior')
else:
    print('De menor')

print('fim')
