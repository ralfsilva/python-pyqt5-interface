from PyQt5 import uic, QtWidgets

def verificacao():

    ano = float(bissexto.valor_lineEdit.text())

    if ano % 4 == 0:
        if (ano % 100 == 0):
            if (ano % 400 == 0):
                bissexto.res_label.setText("O ano é bissexto tem 366 dias.")
    else:
        bissexto.res_label.setText("O ano não é bissexto tem 365 dias.")


app = QtWidgets.QApplication([])
bissexto = uic.loadUi("decisao-17.ui")
bissexto.pb_verificar.clicked.connect(verificacao)
bissexto.show()
app.exec()