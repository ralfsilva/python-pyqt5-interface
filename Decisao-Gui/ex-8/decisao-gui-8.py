from PyQt5 import uic, QtWidgets

produto1 = 0
produto2 = 0
produto3 = 0

def verificacao():
    global produto1
    global produto2
    global produto3

    produto1 = float(produto.lineEdit_n1.text())
    produto2 = float(produto.lineEdit_n2.text())
    produto3 = float(produto.lineEdit_n3.text())

    menor()

def menor():
    global produto1
    global produto2
    global produto3

    barato = produto1

    if produto2 < barato:
        barato = produto2
    if produto3 < barato:
        barato = produto3

    roundBarato = round(barato, 2)
    roundBarato = str(roundBarato)
    produto.label_verificar_2.setText(f'R$ {roundBarato} é o menor preço.')


app = QtWidgets.QApplication([])
produto = uic.loadUi("decisao-8.ui")
produto.pb_verificar.clicked.connect(verificacao)
produto.show()
app.exec()