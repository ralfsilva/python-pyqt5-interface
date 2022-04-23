from PyQt5 import uic, QtWidgets

def verificacao():

    numero = int(verifica.lineEdit.text())

    if numero % 2 == 0:
        verifica.label_verificar.setText("Número par.")
    else:
        verifica.label_verificar.setText("Número impar.")


app = QtWidgets.QApplication([])
verifica = uic.loadUi("decisao-22.ui")
verifica.pb_verificar.clicked.connect(verificacao)
verifica.show()
app.exec()