from PyQt5 import uic, QtWidgets

def verificacao():

    lado1 = float(triangulo.lineEdit_lado1.text())
    lado2 = float(triangulo.lineEdit_lado2.text())
    lado3 = float(triangulo.lineEdit_lado3.text())

    if ((lado1 + lado2) > lado3) or ((lado2 + lado3) > lado1) or ((lado1 + lado3) > lado2):
        if lado1 == lado2 == lado3:
            triangulo.label_verificar.setText("Triângulo Equilátero")

        elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
            triangulo.label_verificar.setText("Triângulo isósceles")
            
        elif (lado1 != lado2) and (lado2 != lado3) and (lado1 != lado3):
            triangulo.label_verificar.setText("Triângulo Escaleno")

    else:
        triangulo.label_verificar.setText("Não é um Triângulo!")

app = QtWidgets.QApplication([])
triangulo = uic.loadUi("decisao-15.ui")
triangulo.pb_verificar.clicked.connect(verificacao)
triangulo.show()
app.exec()