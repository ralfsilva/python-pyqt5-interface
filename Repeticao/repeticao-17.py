fat = int(input("Digite o número para ser mostrado o Fatorial: "))

res = count = 1

while count <= fat:
    res *= count
    count += 1
    print (res)
print ("{}! equivale a: {}".format(fat, res))