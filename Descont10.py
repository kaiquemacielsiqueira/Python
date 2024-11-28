valor = float(input('Digite o valor de um item: '))
qtd = int(input('Digite a quantidade: '))
tot = valor*qtd
descont = tot*0.1
total_final = tot - descont
print(f'Total final com desconto R$: {total_final:.2f}')