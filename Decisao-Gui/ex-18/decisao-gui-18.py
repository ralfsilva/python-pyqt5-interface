from PyQt5 import uic, QtWidgets

def verificacao():

    dia = int(data.lineEdit_dia.text())
    mes = int(data.lineEdit_mes.text())
    ano = int(data.lineEdit_ano.text())



    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia >= 1 and dia <= 31:            
            data.label_verificar.setText(f'A data {dia}/{mes}/{ano} é válida.')
        else:
            data.label_verificar.setText(f'A data {dia}/{mes}/{ano} é inválida.')
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia >= 1 and dia <= 30:
            data.label_verificar.setText(f'A data {dia}/{mes}/{ano} é válida.')
        else:
            data.label_verificar.setText(f'A data {dia}/{mes}/{ano} é inválida.')
    elif mes == 2:
        if dia >= 1 and dia <= 28:
            data.label_verificar.setText(f'A data {dia}/{mes}/{ano} é válida.')
        elif dia == 29:
            if ano % 4 == 0:
                data.label_verificar.setText(f'A data {dia}/{mes}/{ano} é válida e o ano é bissexto.')
            else:
                data.label_verificar.setText(f'A data {dia}/{mes}/{ano} é inválida pois o ano não é bissexto.')   
    else:
        data.label_verificar.setText(f'A data {dia}/{mes}/{ano} é inválida.')
        

app = QtWidgets.QApplication([])
data = uic.loadUi("decisao-18.ui")
data.pb_verificar.clicked.connect(verificacao)
data.show()
app.exec()