from PyQt5 import uic, QtWidgets

total = 0
produto1 = 0
produto2 = 0
troco = 0
dinheiro = 0

def produtos_parte1():
    global total
    global produto1
    global produto2

    # Variável recebendo valor float pois está herdando o string da função proxima_compra
    total = float(total)
    
    # Variável total sendo zerada para não acrescentar o valor da compra anterior à nova compra
    total = 0
    sTotal = ''

    produto1 = float(produto.lineEdit_product1.text())
    total += produto1
    produto2 = float(produto.lineEdit_product2.text())
    total += produto2

    sTotal = str(total)
    produto.product_3.setText("R$ 0")
    produto.label_totalResult.setText("R$ " + sTotal)
    
# Função que é implementada após o botão total
def produtos_parte2():
    global total
    global dinheiro
    global troco

    dinheiro = float(produto.lineEdit_dinheiro.text())
    troco = dinheiro - total
    troco = str(troco)

    # Verificação se o valor recebido como dinheiro é possível para pagar a compra dos produtos
    if dinheiro < total:
        produto.troco.setText("Valor insuficiente para\npagar a compra.")
    else:
        produto.troco.setText("R$ " + troco)

# Função para que seja feita outra compra
def proxima_compra():
    global produto1
    global produto2
    global total
    global dinheiro

    produto1 = str(produto1)
    produto2 = str(produto2)
    total = str(total)
    dinheiro = str(dinheiro)

    produto.lineEdit_product1.setText("")
    produto.lineEdit_product2.setText("")
    produto.product_3.setText("")
    produto.label_totalResult.setText("")
    produto.lineEdit_dinheiro.setText("")
    produto.troco.setText("")


app = QtWidgets.QApplication([])
produto = uic.loadUi("repeticao-31.ui")
produto.pb_produto.clicked.connect(produtos_parte1)
produto.pb_pagar.clicked.connect(produtos_parte2)
produto.pb_proximaCompra.clicked.connect(proxima_compra)
produto.show()
app.exec()