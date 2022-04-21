from PyQt5 import uic, QtWidgets    

def main():
    item = 3
    parteInteira = 5
    parteFracionada = 97
    count = 2

    print ("Lojas Quase Dois - Tabela de preços\n 1 - R$ 1,99\n 2 - R$ 3,99\n")

    while count != 49:
        item += 1
        parteFracionada -= 1
        parteInteira += 2
        count += 1

        print (f'{item} - R$ {parteInteira},{parteFracionada}')
        

app = QtWidgets.QApplication([])
lista = uic.loadUi("29_gui.ui")
lista.show()
app.exec()