from PyQt5 import uic, QtWidgets

def informacoes():

    nome = info.nome_lineEdit.text()
    idade = int(info.idade_lineEdit.text())
    salario = float(info.salario_lineEdit.text())
    sexo = info.sexo_lineEdit.text()
    estadoCivil = info.eCivil_lineEdit.text()

    if len(nome) <= 3:
        info.nomeResp_label.setText("Digite mais de 3 Caracteres.")
        info.nome_lineEdit.setText("")
    else:
        info.nomeResp_label.setText("Ok!")

    if idade > 0 and idade < 150:
        idade = str(idade)
        info.idadeResp_label.setText("Ok!")
    else:
        idade = str(idade)
        info.idadeResp_label.setText("Digite uma idade entre 0 e 150.")
        info.idade_lineEdit.setText("")

    if salario < 0:
        salario = str(salario)
        info.salarioResp_label.setText("Digite um Salário maior que 0.")
        info.salario_lineEdit.setText("")
    else:
        salario = str(salario)
        info.salarioResp_label.setText("Ok!")

    if sexo == 'f' or sexo == 'm':
        info.sexoResp_label.setText("Ok!")
    else:
        info.sexoResp_label.setText("Digite (f)eminino ou (m)asculino.")
        info.sexo_lineEdit.setText("")

    if estadoCivil == 's' or estadoCivil == 'c' or estadoCivil == 'v' or estadoCivil == 'd':
        info.eCivilResp_label.setText("Ok!")
    else:
        info.eCivilResp_label.setText("Digite (s)olteiro, (c)asado, (v)iuvo ou (d)ivorciado.")
        info.eCivil_lineEdit.setText("")

app = QtWidgets.QApplication([])
info = uic.loadUi("repeticao-3.ui")
info.pb_validacao.clicked.connect(informacoes)
info.show()
app.exec()