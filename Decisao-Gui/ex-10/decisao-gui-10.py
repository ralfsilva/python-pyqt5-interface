from PyQt5 import uic, QtWidgets

def verificacao():

    verifica = letra.lineEdit.text()

    if verifica == 'm' or verifica == 'M':
        letra.label_verificar.setText("Bom dia!")
    elif verifica == 'v' or verifica == 'V':
        letra.label_verificar.setText("Boa Tarde!")
    elif verifica == 'n' or verifica == 'N':
        letra.label_verificar.setText("Boa Noite!")
    else:
        letra.label_verificar.setText("Valor inválido!")

app = QtWidgets.QApplication([])
letra = uic.loadUi("decisao-10.ui")
letra.pb_verificar.clicked.connect(verificacao)
letra.show()
app.exec()