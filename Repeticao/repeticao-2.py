name = input("Digite o nome de usuário: ")
password = input("Digite uma senha: ")

while password == name:
    print ("ERRO !!!")
    password = input("Digite uma senha diferente: ")

print ("\nNome de Usuário: {} \nSenha: {}".format(name, password))