from PyQt5 import uic, QtWidgets

def verificacao():

    nota1 = float(notas.lineEdit_nota1.text())
    nota2 = float(notas.lineEdit_nota2.text())
    nota3 = float(notas.lineEdit_nota3.text())

    media = (nota1 + nota2 + nota3) / 3

    if media >= 7.0 and media <= 9.9:
        notas.label_verificar.setText(f'Aprovado - Nota {media:.1f}')
    elif media >= 0.0 and media <= 7.0:
        notas.label_verificar.setText(f'Reprovado - Nota {media:.1f}')
    elif media == 10.0:
        notas.label_verificar.setText(f'Aprovado com Distinção - Nota {media:.1f}')
    else:
        notas.label_verificar.setText(f'Nota inválida.')


app = QtWidgets.QApplication([])
notas = uic.loadUi("decisao-20.ui")
notas.pb_verificar.clicked.connect(verificacao)
notas.show()
app.exec()