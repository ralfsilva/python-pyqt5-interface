from PyQt5 import uic, QtWidgets
import math

def verificacao():

    a = float(raizQuadrada.lineEdit_lado1.text())

    if a != 0:  

        b = float(raizQuadrada.lineEdit_lado2.text())
        c = float(raizQuadrada.lineEdit_lado3.text())
        
        delta = (math.pow(b, 2) - 4 * a * c)

        bhaskaraPositivo = (- b + delta ** (1/2)) / (2 * a)
        bhaskaraNegativo = (- b - delta ** (1/2)) / (2 * a)

        strDelta = str(delta)

        if delta < 0:
            raizQuadrada.label_verificar.setText("A equação não possui raizes reais, pois o Delta é negativo. Delta = " + strDelta)
        
        elif delta == 0:
            raizQuadrada.label_verificar.setText("A equação possui apenas uma raiz real. Delta = " + strDelta)

        elif delta > 0:
            raizQuadrada.label_verificar.setText("A equação possui duas raizes reais. Raiz 1: {:.2f} - Raiz 2: {:.2f}".format(bhaskaraPositivo, bhaskaraNegativo))
    
    else:
        raizQuadrada.label_verificar.setText("Não é uma Raiz Quadrada.")


app = QtWidgets.QApplication([])
raizQuadrada = uic.loadUi("decisao-16.ui")
raizQuadrada.pb_verificar.clicked.connect(verificacao)
raizQuadrada.show()
app.exec()