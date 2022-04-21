from PyQt5 import uic, QtWidgets

precoPao = 0
item = 0

# Função que adiciona cada item
def listar_dados():
    global precoPao
    global item    

    item += 1
    precoPao += 0.18

    lista.listWidget.addItem(f'{item} - R$ {precoPao:.2f}')

    # A condição não deixa que o item seja maior que 50
    if item > 50:
        lista.listWidget.clear()
        item = 0
        precoPao = 0


app = QtWidgets.QApplication([])
lista = uic.loadUi("repeticao-30.ui")
lista.pb_addItem.clicked.connect(listar_dados)
lista.show()
app.exec()