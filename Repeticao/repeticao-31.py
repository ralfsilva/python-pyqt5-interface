item = 3
totalValue = 0
add = 's'

print ("Lojas Tabajara")

while add == 's':
    
    productOne = float(input("Produto 1: R$"))
    totalValue += productOne
    productTwo = float(input("Produto 2: R$"))
    totalValue += productTwo

    while add == 's':
        add = input("Adicionar mais algum produto? (s)im ou (n)ão.")

        if add == 's':
            askProduct = float(input(f'Produto {item}: R$ '))
            totalValue += askProduct
            item += 1
    
    if add != 's':
        print (f'Produto {item}: R$ 0 ')

receiveMoney = float(input(" Dinheiro: R$ "))
payBack = receiveMoney - totalValue
print (f'Troco: R$ {payBack:.2f}')