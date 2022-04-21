from PyQt5 import uic, QtWidgets

def verificacao():

    valor = float(val.valor_lineEdit.text())

    if (valor >= 0):
        val.res_label.setText("Positivo!")
    else:
        val.res_label.setText("Negativo!")

app = QtWidgets.QApplication([])
val = uic.loadUi("decisao-2.ui")
val.pb_verificar.clicked.connect(verificacao)
val.show()
app.exec()