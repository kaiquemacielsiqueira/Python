p = int(input('Digite o valor de P: '))
q = int(input('Digite o valor de q: '))
contador = 0

while p>=q:
    p=p-q
    contador += 1
print(f'o quociente da divisão de p sobre q é {contador}')
