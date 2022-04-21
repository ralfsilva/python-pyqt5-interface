from PyQt5 import uic, QtWidgets

def verificacao():

    nota1 = float(notas.lineEdit_nota1.text())
    nota2 = float(notas.lineEdit_nota2.text())

    media = (nota1 + nota2) / 2

    if media >= 7.0 and media <= 9.9:
        media = str(media)
        notas.label_verificar.setText("Aprovado")
    elif media >= 0.0 and media <= 7.0:
        media = str(media)
        notas.label_verificar.setText("Reprovado")
    elif media == 10.0:
        media = str(media)
        notas.label_verificar.setText("Aprovado com Distinção")


app = QtWidgets.QApplication([])
notas = uic.loadUi("decisao-5.ui")
notas.pb_verificar.clicked.connect(verificacao)
notas.show()
app.exec()