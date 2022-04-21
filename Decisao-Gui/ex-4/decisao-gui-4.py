from PyQt5 import uic, QtWidgets

def verificacao():

    verifica = letra.lineEdit.text()

    if (verifica == 'a' or verifica == 'e' or verifica == 'i'  or verifica == 'o' or verifica == 'u'):
        letra.label_verificar.setText("Vogal")
    else:
        letra.label_verificar.setText("Consoante")


app = QtWidgets.QApplication([])
letra = uic.loadUi("decisao-4.ui")
letra.pb_verificar.clicked.connect(verificacao)
letra.show()
app.exec()