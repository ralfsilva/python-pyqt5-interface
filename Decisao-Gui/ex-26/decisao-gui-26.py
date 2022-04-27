from PyQt5 import uic, QtWidgets

def verificacao():

    litros = int(verifica.lineEdit.text())
    tipo = verifica.lineEdit_2.text()

    if tipo == 'A' or tipo == 'a':
        if litros <= 20:
            valor = float(litros * 1.90)
            total = float(valor - (valor * 0.03))
            verifica.label_verificar.setText(f'O valor a ser pago no álcool: R$ {total:.2f}')
        elif litros > 20:
            valor = float(litros * 1.90)
            total = float(valor - (valor * 0.05))
            verifica.label_verificar.setText(f'O valor a ser pago no álcool: R$ {total:.2f}')
    elif tipo == 'G' or tipo == 'g':
        if litros <= 20:
            valor = float(litros * 2.50)
            total = float(valor - (valor * 0.04))
            verifica.label_verificar.setText(f'O valor a ser pago na gasolina: R$ {total:.2f}')
        elif litros > 20:
            valor = float(litros * 2.50)
            total = float(valor - (valor * 0.06))
            verifica.label_verificar.setText(f'O valor a ser pago na gasolina: R$ {total:.2f}')
    else:
        verifica.label_verificar.setText("Escolha inválida! Tente novamente.")


app = QtWidgets.QApplication([])
verifica = uic.loadUi("decisao-26.ui")
verifica.pb_verificar.clicked.connect(verificacao)
verifica.show()
app.exec()