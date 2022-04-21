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

    maior()
    menor()

def maior():
    global numero1
    global numero2
    global numero3

    oMaior = numero1

    if numero2 > oMaior:
        oMaior = numero2
    if numero3 > oMaior:
        oMaior = numero3

    oMaior = str(oMaior)
    verifica.label_verificar.setText(f'{oMaior} é o maior.')

def menor():
    global numero1
    global numero2
    global numero3

    oMenor = numero1

    if numero2 < oMenor:
        oMenor = numero2
    if numero3 < oMenor:
        oMenor = numero3

    oMenor = str(oMenor)
    verifica.label_verificar_2.setText(f'{oMenor} é o menor.')


app = QtWidgets.QApplication([])
verifica = uic.loadUi("decisao-7.ui")
verifica.pb_verificar.clicked.connect(verificacao)
verifica.show()
app.exec()