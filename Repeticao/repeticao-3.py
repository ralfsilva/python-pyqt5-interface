nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
salario = float(input("Digite o seu salário: "))
sexo = input("Digite o seu Sexo (m ou f): ")
estadoCivil = input("Digite o seu estado civil: \ns = Solteiro \nc = Casado \nv = viúvo \nd = Divorciado \n")

while len(nome) <= 3:
    print ("Erro! Tente novamente.")
    nome = input("Digite o seu nome: ")

while idade < 0 or idade > 150:
    print ("Erro! Tente novamente.")
    idade = int(input("Digite a sua idade: "))

while salario < 0:
    print ("Erro! Tente novamente.")
    salario = float(input("Digite o seu salário: "))

while sexo != 'm' and sexo != 'f':
    print ("Erro! Tente novamente.")
    sexo = input("Digite o seu Sexo (m ou f): ")

while estadoCivil != 's' and estadoCivil != 'c' and estadoCivil != 'v' and estadoCivil != 'd':
    print ("Erro! Tente novamente.")
    estadoCivil = input("Digite o seu estado civil: \ns = Solteiro \nc = Casado \nv = viúvo \nd = Divorciado \n")

print ("Nome: {} - Idade: {} - Salário: {} - Sexo: {} - Estado Cívil: {}".format(nome, idade, salario, sexo, estadoCivil))