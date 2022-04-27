print ("Lojas Quase Dois - Tabela de preços\n 1 - R$ 1,99\n 2 - R$ 3,99\n")
item = 3
parteInteira = 5
parteFracionada = 97
count = 2

while count != 50:
    print (f'{item} - R$ {parteInteira},{parteFracionada}')
    item += 1
    parteFracionada -= 1
    parteInteira += 2
    count += 1