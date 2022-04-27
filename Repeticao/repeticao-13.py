base = int(input("Digite a base: "))
exp = int(input("Digite o expoente: "))

mult = 1

while mult != exp:
    mult += 1
    print ("{} elevado ao expoente {} = {}".format(base, exp, base ** mult))