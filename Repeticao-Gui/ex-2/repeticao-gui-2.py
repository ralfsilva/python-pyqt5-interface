from PyQt5 import uic, QtWidgets

def user():

    nome = usuario.nome_lineEdit.text()
    senha = usuario.senha_lineEdit.text()

    if senha == nome:
        usuario.mostrar_label.setText("Erro !!! Digite uma senha diferente do nome")
        usuario.nome_lineEdit.setText("")
        usuario.senha_lineEdit.setText("")

app = QtWidgets.QApplication([])
usuario = uic.loadUi("repeticao-2.ui")
usuario.pb_criar.clicked.connect(user)
usuario.show()
app.exec()