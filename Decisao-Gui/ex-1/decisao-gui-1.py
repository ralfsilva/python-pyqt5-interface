from PyQt5 import uic, QtWidgets

def maior():

    numero1 = float(oMaior.lineEdit.text())
    numero2 = float(oMaior.lineEdit_2.text())

    if (numero1 > numero2):
        numero1 = str(numero1)
        oMaior.oMaior_label.setText(numero1)
    else:
        numero2 = str(numero2)
        oMaior.oMaior_label.setText(numero2)


app = QtWidgets.QApplication([])
oMaior = uic.loadUi("decisao-1.ui")
oMaior.pb_oMaior.clicked.connect(maior)
oMaior.show()
app.exec()