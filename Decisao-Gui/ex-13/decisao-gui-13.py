from PyQt5 import uic, QtWidgets

def verificacao():

    dia = int(semana.lineEdit.text())

    if dia == 1:
        semana.res_label.setText("1 -  Domingo")
    elif dia == 2:
        semana.res_label.setText("2 - Segunda")
    elif dia == 3:
        semana.res_label.setText("3 - Terça")
    elif dia == 4:
        semana.res_label.setText("4 - Quarta")
    elif dia == 5:
        semana.res_label.setText("5 - Quinta")
    elif dia == 6:
        semana.res_label.setText("6 - Sexta")
    elif dia == 7:
        semana.res_label.setText("7 - Sábado")
    else:
        semana.res_label.setText("Valor Inválido.")


app = QtWidgets.QApplication([])
semana = uic.loadUi("decisao-13.ui")
semana.pb_verificar.clicked.connect(verificacao)
semana.show()
app.exec()