from PyQt5 import uic, QtWidgets

# Primeiramente Testar os 2 numeros e clicar no botão verificar, após a verificação, digitar qual operação realizar e verificar

def verificacao():

    numero = float(verifica.lineEdit.text())
    numero2 = float(verifica.lineEdit_2.text())

    escolha = verifica.lineEdit_Escolha.text()

    verifica.label_operacao.setText("Escolha a operação a ser feita: \n\na. par ou imper. \n\nb. positivo ou negativo \n\nc. inteiro ou decimal") 

    if escolha == 'a' or escolha == 'A':
        numero = int(numero)
        numero2 = int(numero2)

        if numero % 2 == 0:
            verifica.label_verificar.setText(f'Número par: {numero}')
        elif numero % 2 == 1:
            verifica.label_verificar.setText(f'Número Impar: {numero}')
        if numero2 % 2 == 0:
            verifica.label_verificar_2.setText(f'Número par: {numero2}')
        elif numero2 % 2 == 1:
            verifica.label_verificar_2.setText(f'Número Impar: {numero2}')
        

    if escolha == 'b' or escolha == 'B':
        
        if numero > 0:
            verifica.label_verificar.setText(f'Número Positivo: {numero}')
        elif numero < 0:
            verifica.label_verificar.setText(f'Número Negativo: {numero}')
        else:
            verifica.label_verificar.setText(f'Número Nulo: {numero}, tente novamente')
        if numero2 > 0:
            verifica.label_verificar_2.setText(f'Número Positivo: {numero2}')
        elif numero2 < 0:
            verifica.label_verificar_2.setText(f'Número Negativo: {numero2}')
        else:
            verifica.label_verificar_2.setText(f'Número Nulo: {numero2}, tente novamente')

    if escolha == 'c' or escolha == 'C':

        if numero == round(numero) or numero == round(numero) and numero < 0:
            verifica.label_verificar.setText(f'Número inteiro: {numero}')
        else:
            verifica.label_verificar.setText(f'Número Decimal: {numero}')
        if numero2 == round(numero2) or numero2 == round(numero2) and numero2 < 0:
            verifica.label_verificar_2.setText(f'Número inteiro: {numero2}')
        else:
            verifica.label_verificar_2.setText(f'Número Decimal: {numero2}')


app = QtWidgets.QApplication([])
verifica = uic.loadUi("decisao-24.ui")
verifica.pb_verificar.clicked.connect(verificacao)
verifica.show()
app.exec()