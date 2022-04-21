from PyQt5 import uic, QtWidgets

def notas():
  
    nota = float(note.lineEdit.text())

    if nota >= 0 and nota <= 10:
        text = str(nota)
        note.label_nota.setText("Nota correta - " + text)
    else:
        note.label_nota.setText("Nota Incorreta.")


app = QtWidgets.QApplication([])
note = uic.loadUi("repeticao-1.ui")
note.pb_nota.clicked.connect(notas)
note.show()
app.exec()