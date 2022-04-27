from PyQt5 import uic, QtWidgets

def verificacao():
    cem = 0
    cinq = 0
    dez = 0
    cinco = 0
    um = 0

    saque = int(caixa.lineEdit.text())

    total = saque

    if saque >= 10 and saque <= 600:
        while saque >= 100:
            cem += 1
            saque -= 100
        while saque >= 50 and saque < 100:
            cinq += 1
            saque -= 50
        while saque >= 10 and saque < 50:
            dez += 1
            saque -= 10
        while saque >= 5 and saque < 10:
            cinco += 1
            saque -= 5
        while saque >= 1 and saque < 5:
            um += 1
            saque -= 1

        caixa.label_verificar.setText(f'Para sacar a quantia de R$ {total}: \n\nNotas de 100: {cem} nota(s) de 100. \n\nNotas de 50: {cinq} nota(s) de 50. \n\nNotas de 10: {dez} nota(s) de 10. \n\nNotas de 5: {cinco} nota(s) de 5. \n\nNotas de 1: {um} nota(s) de 1.')
    else:
        caixa.label_verificar.setText(f'Digite um valor para saque entre 10 e 600 reais.')

        
app = QtWidgets.QApplication([])
caixa = uic.loadUi("decisao-21.ui")
caixa.pb_verificar.clicked.connect(verificacao)
caixa.show()
app.exec()