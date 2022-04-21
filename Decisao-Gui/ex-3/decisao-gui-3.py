from PyQt5 import uic, QtWidgets

def verificacao():

    letra = sexo.lineEdit.text()

    if (letra == 'F' or letra == 'f' or letra == 'm' or letra == 'M'):
        sexo.label_verificar.setText("Sexo inválido.")
    else:
        sexo.label_verificar.setText("Sexo válido.")


app = QtWidgets.QApplication([])
sexo = uic.loadUi("decisao-3.ui")
sexo.pb_verificar.clicked.connect(verificacao)
sexo.show()
app.exec()