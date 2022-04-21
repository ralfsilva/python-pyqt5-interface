from PyQt5 import uic, QtWidgets

numero1 = 0
numero2 = 0
numero3 = 0

def verificacao():
    global numero1
    global numero2
    global numero3

    numero1 = float(verifica.lineEdit_n1.text())
    numero2 = float(verifica.lineEdit_n2.text())
    numero3 = float(verifica.lineEdit_n3.text())

    decrescente()


def decrescente():
    global numero1
    global numero2
    global numero3

    if numero3 > numero2:
        aux = numero3
        numero3 = numero2
        numero2 = aux
    if numero2 > numero1:
        aux = numero2
        numero2 = numero1
        numero1 = aux
    if numero3 > numero2:
        aux = numero3
        numero3 = numero2
        numero2 = aux

    primeiro = str(numero3)
    segundo = str(numero2)
    terceiro = str(numero1)

    verifica.label_verificar.setText(terceiro + " - " + segundo + " - " + primeiro)



app = QtWidgets.QApplication([])
verifica = uic.loadUi("decisao-9.ui")
verifica.pb_verificar.clicked.connect(verificacao)
verifica.show()
app.exec()