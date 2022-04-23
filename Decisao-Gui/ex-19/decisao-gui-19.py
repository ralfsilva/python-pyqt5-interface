from PyQt5 import uic, QtWidgets

def verificacao():

    numero = int(mil.lineEdit.text())
    total = numero

    centena = 0
    dezena = 0
    unidade = 0

    sUnidades = ''
    sDezenas = ''
    sCentenas = ''

    if numero < 1000 and numero > 0:
        while numero > 99:
            centena += 1
            numero -= 100

        while numero > 9:
            dezena += 1
            numero -= 10

        while numero >= 1:
            unidade += 1
            numero -= 1

        if unidade == 1:
            sUnidades = 'unidade'
        elif unidade > 1 and unidade < 10:
            sUnidades = 'unidades'

        if dezena == 1:
            sDezenas = 'dezena'
        elif dezena > 1 and dezena < 10:
            sDezenas = 'dezenas'
            
        if centena == 1:
            sCentenas = 'centena'
        elif centena > 1 and centena < 10:
            sCentenas = 'centenas'

        if (unidade >= 1 and unidade <= 9):
            mil.label_verificar.setText(f'{total} = {unidade} {sUnidades}')

        if (dezena >= 1 and dezena <= 9):
            mil.label_verificar.setText(f'{total} = {dezena} {sDezenas}')

        if (centena >= 1 and centena <= 9):
            mil.label_verificar.setText(f'{total} = {centena} {sCentenas}')

        if (unidade >= 1 and unidade <= 9) and (dezena >= 1 and dezena <= 9):
            mil.label_verificar.setText(f'{total} = {dezena} {sDezenas} e {unidade} {sUnidades}')

        if (unidade >= 1 and unidade <= 9) and (dezena >= 1 and dezena <= 9) and (centena >= 1 and centena <= 9):
            mil.label_verificar.setText(f'{total} = {centena} {sCentenas}, {dezena} {sDezenas} e {unidade} {sUnidades}')






    else:
        mil.label_verificar.setText(f'Digite um Número maior que 0 e menor que 1000.')


app = QtWidgets.QApplication([])
mil = uic.loadUi("decisao-19.ui")
mil.pb_verificar.clicked.connect(verificacao)
mil.show()
app.exec()