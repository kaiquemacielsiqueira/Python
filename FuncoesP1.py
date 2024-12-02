def obter_nome(): #Definindo a função
    nome = input('Digite seu nome: ')
    return nome

nome_digitado = obter_nome() #Chamando a função
print(f'Olá, {nome_digitado}')