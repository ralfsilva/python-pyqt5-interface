from PyQt5 import uic, QtWidgets

def verificacao():
    valor = 0

    morango = int(verifica.lineEdit.text())
    maca = int(verifica.lineEdit_2.text())

    frutas = morango + maca

    if morango <= 5:
        valor += float(morango * 2.50)
    if morango > 5 and morango <= 11:
        valor += float(morango * 2.20)
    if maca <= 5:
        valor += float(maca * 1.80)
    if maca > 5 and morango <= 16:
        valor += float(maca * 1.50)
    if frutas > 8 or valor >= 25.00:
        valor = valor - (valor * 0.1)

    verifica.label_verificar.setText(f'O valor total: R$ {valor:.2f}')


app = QtWidgets.QApplication([])
verifica = uic.loadUi("decisao-27.ui")
verifica.pb_verificar.clicked.connect(verificacao)
verifica.show()
app.exec()