print ("Preço do pão: R$ 0.18 \nPanificadora Pão de ontem - Tabela de preços \n1 - R$ 0.18 \n2 - R$ 0.36")

item = 3
precoPao = 0.54
count = 2

while count != 50:
    print (f'{item} - R$ {precoPao:.2f}')
    item += 1
    precoPao += 0.18
    count += 1