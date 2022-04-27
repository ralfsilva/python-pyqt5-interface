x = 1
par = impar = 0

while x != 11:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        par += 1
    elif num % 2 == 1:
        impar += 1    

    x += 1

print ("São {} número pares e {} números impares.".format(par, impar))