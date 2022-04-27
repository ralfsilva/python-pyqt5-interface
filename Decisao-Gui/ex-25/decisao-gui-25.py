from PyQt5 import uic, QtWidgets

def verificacao():
    count = 0

    verifica.label_verificar.setText("Responda o questionário investigativo sobre o Crime corretamente com 0 ou 1. \n")

    q1 = int(verifica.lineEdit.text())
    if q1 == 1:
        count += 1
    else:
        count += 0

    q2 = int(verifica.lineEdit_2.text())
    if q2 == 1:
        count += 1
    else:
        count += 0

    q3 = int(verifica.lineEdit_3.text())
    if q3 == 1:
        count += 1
    else:
        count += 0

    q4 = int(verifica.lineEdit_4.text())
    if q4 == 1:
        count += 1
    else:
        count += 0

    q5 = int(verifica.lineEdit_5.text())
    if q5 == 1:
        count += 1
    else:
        count += 0

    if count == 1:
        verifica.label_verificar.setText("A pessoa é inocente.")
    elif count == 2:
        verifica.label_verificar.setText("Esta pessoa é suspeita.")
    elif count == 3 or count == 4:
        verifica.label_verificar.setText("Esta pessoa é cúmplice.")
    elif count == 5:
        verifica.label_verificar.setText("Esta pessoa é o assassino!")


app = QtWidgets.QApplication([])
verifica = uic.loadUi("decisao-25.ui")
verifica.pb_verificar.clicked.connect(verificacao)
verifica.show()
app.exec()