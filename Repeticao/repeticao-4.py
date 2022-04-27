a = 0.03
paisA = 80000

b = 0.015
paisB = 200000
italia = brasil = ano = 0

pais = True

while paisA < paisB:
    italia = int(paisA * a)
    paisA += italia

    brasil = int(paisB * b)
    paisB += brasil
    ano += 1

    print ("A - {} - B - {}".format(paisA, paisB))
print ("Anos para igualar os habitantes dos países: {} anos.".format(ano))