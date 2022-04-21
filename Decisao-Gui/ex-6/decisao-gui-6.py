from PyQt5 import uic, QtWidgets

def verificacao():

    numero1 = float(maior.lineEdit_n1.text())
    numero2 = float(maior.lineEdit_n2.text())
    numero3 = float(maior.lineEdit_n3.text())

    if numero1 > numero2 and numero1 > numero3:
        numero1 = str(numero1)
        maior.label_verificar.setText("O Número 1 é o Maior")
    elif numero2 > numero1 and numero2 > numero3:
        numero2 = str(numero2)
        maior.label_verificar.setText("O Número 2 é o Maior")
    else:
        numero3 = str(numero3)
        maior.label_verificar.setText("O Número 3 é o Maior")
    


app = QtWidgets.QApplication([])
maior = uic.loadUi("decisao-6.ui")
maior.pb_verificar.clicked.connect(verificacao)
maior.show()
app.exec()