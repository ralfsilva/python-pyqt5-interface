x = total = 0

while x != 5:
    x += 1
    number = float(input("Digite um número: "))
    total += number

media = total / 5

print (f'Média dos números {media:.1f}')