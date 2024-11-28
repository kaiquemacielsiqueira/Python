num = int(input('Digite o numero para que eu te diga a tabuada: '))
print(f"Tabuada do {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")