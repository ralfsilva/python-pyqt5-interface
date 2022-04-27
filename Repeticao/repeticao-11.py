inter1 = int(input("Digite o primeiro número inteiro:"))
inter2 = int(input("Digite o segundo número inteiro:"))
copy = inter1
seq = True
print(copy)

if inter1 > inter2:
    while seq:
        inter1 -= 1
        print (inter1)
        if inter1 == inter2:
            seq = False    

if inter1 < inter2:
    while seq:
        inter1 += 1
        print (inter1)
        if inter1 == inter2:
            seq = False

total = copy + inter2
print ("A sequência entre {} e {} e a soma {}".format(copy, inter2, total))