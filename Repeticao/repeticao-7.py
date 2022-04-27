x = maior = 0

while x != 5:
    x += 1
    ask = float(input("Digite um número: "))
    
    if ask > maior:
        maior = ask
        print (maior)

print (f'Este é o maior número: {maior:.0f}')