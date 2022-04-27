valida = validaB = True

while valida:    
    paisA = float(input("Digite a população do Pais A, entre 50.000 - 100.000: "))
    if paisA >= 50.000 and paisA <= 100.000:
        valida = False
    else:
        print ("Erro! Tente novamente.")
        valida = True

while validaB:
    paisB = float(input("Digite a população do Pais B, entre 200.000 - 300.000: "))
    if paisB >= 200.000 and paisB <= 300.000:
        validaB = False
    else:
        print ("Erro! Tente novamente.")
        valida = True

taxaA = float(input("Digite a taxa de crescimento do País A: "))
taxaB = float(input("Digite a taxa de crescimento do País B: "))

taxaA = taxaA / 100
taxaB = taxaB / 100

repetir = True
ano = 0

while paisA < paisB:
    eua = paisA * taxaA
    paisA += eua

    brasil = paisB * taxaB
    paisB += brasil

    ano += 1

    print (f'A - {paisA:.3f} - B - {paisB:.3f}')

while repetir:
    repeat = int(input("Deseja Repetir? \n1 - Sim \n2 - Não"))
    ano = 0
    if repeat == 1:
        while paisA < paisB:
            paisA = float(input("Digite a população do Pais A, entre 50.000 - 100.000: "))
            paisB = float(input("Digite a população do Pais B, entre 200.000 - 300.000: "))

            taxaA = float(input("Digite a taxa de crescimento do País A: "))
            taxaB = float(input("Digite a taxa de crescimento do País B: "))

            taxaA = taxaA / 100
            taxaB = taxaB / 100

            eua = paisA * taxaA
            paisA += eua

            brasil = paisB * taxaB
            paisB += brasil

            ano += 1

            print (f'A - {paisA:.3f} - B - {paisB:.3f}')
    else:
        repetir = False

print ("Obrigado pela participação!")