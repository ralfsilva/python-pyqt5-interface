from PyQt5 import uic, QtWidgets

def verificacao():
    valor = 0

    tipoCarne = int(verifica.lineEdit.text())

    quantidadeCarne = int(verifica.lineEdit_2.text())

    if tipoCarne == 1:
        nomeCarne = 'Filé Duplo'
        if quantidadeCarne <= 5:
            valor = quantidadeCarne * 4.90
        elif quantidadeCarne > 5:
            valor = quantidadeCarne * 5.80

    elif tipoCarne == 2: 
        nomeCarne = 'Alcatra'
        if quantidadeCarne <= 5:
            valor = quantidadeCarne * 5.90
        elif quantidadeCarne > 5:
            valor = quantidadeCarne * 6.80

    elif tipoCarne == 3:
        nomeCarne = 'Picanha'      
        if quantidadeCarne <= 5:
            valor = quantidadeCarne * 6.90
        elif quantidadeCarne > 5:
            valor = quantidadeCarne * 7.80

    tabajara = int(verifica.lineEdit_3.text())
    desconto = valor * 0.05
    precoTotal = valor
    if tabajara == 1:
        tipoPagamento = 'Cartão Tabajara'
        valor = float(valor - (valor * 0.05))
    else:
        tipoPagamento = 'Dinheiro'
        desconto = 0

    verifica.label_verificar.setText(f'Cupom Fiscal \n\nTipo da Carne: {nomeCarne} \nQuantidade: {quantidadeCarne} Kg \nPreço Total: R$ {precoTotal:.2f} \nTipo de Pagamento: {tipoPagamento} \nValor do Desconto: R$ {desconto:.2f} \nValor a Pagar: R$ {valor:.2f}')


app = QtWidgets.QApplication([])
verifica = uic.loadUi("decisao-28.ui")
verifica.pb_verificar.clicked.connect(verificacao)
verifica.show()
app.exec()