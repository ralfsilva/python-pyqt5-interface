from PyQt5 import uic, QtWidgets
import math

a = 0

def verificacao():
    global a

    b = float(raizQuadrada.lineEdit_lado2.text())
    c = float(raizQuadrada.lineEdit_lado3.text())
        
    delta = (math.pow(b, 2) - 4 * a * c)

    bhaskaraPositivo = (- b + delta ** (1/2)) / (2 * a)
    bhaskaraNegativo = (- b - delta ** (1/2)) / (2 * a)

    if delta < 0:
        raizQuadrada.label_verificar.setText(f'A equação não possui raizes reais, pois o Delta é negativo. Delta = {delta}')
        
    elif delta == 0:
        raizQuadrada.label_verificar.setText(f'A equação possui apenas uma raiz real. Delta = {delta}')

    elif delta > 0:
        raizQuadrada.label_verificar.setText(f'A equação possui duas raizes reais. Raiz 1: {bhaskaraPositivo:.2f} - Raiz 2: {bhaskaraNegativo:.2f}')
    
    else:
        raizQuadrada.close()
        # raizQuadrada.label_verificar.setText("Não é uma Raiz Quadrada.")

def verificaA():
    global a

    a = float(raizQuadrada.lineEdit_lado1.text())

    if a != 0:
        raizQuadrada.label_verificar.setText("É uma Raiz Quadrada!")
    else:
        raizQuadrada.close()


app = QtWidgets.QApplication([])
raizQuadrada = uic.loadUi("decisao-16.ui")
raizQuadrada.pb_verificaA.clicked.connect(verificaA)
raizQuadrada.pb_verificar.clicked.connect(verificacao)
raizQuadrada.show()
app.exec()