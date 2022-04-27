from PyQt5 import uic, QtWidgets

def verificacao():

    numero = float(verifica.lineEdit.text())

    if numero == round(numero):
        verifica.label_verificar.setText("Número inteiro.")
    else:
        verifica.label_verificar.setText("Número Decimal.")


app = QtWidgets.QApplication([])
verifica = uic.loadUi("decisao-23.ui")
verifica.pb_verificar.clicked.connect(verificacao)
verifica.show()
app.exec()