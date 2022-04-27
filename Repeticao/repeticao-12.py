tab = int(input("Digite um número para gerar a tabuada: "))

print ("Tabuada do {}: ".format(tab))

mult = 1

while mult != 11 and tab <= 10:
    print ("{} X {} = {}".format(tab, mult, tab * mult))
    mult += 1
