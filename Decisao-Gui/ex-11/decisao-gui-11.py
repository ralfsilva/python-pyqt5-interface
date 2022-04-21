from PyQt5 import uic, QtWidgets

def verificacao():

    salario = float(salarios.lineEdit.text())

    vintePorCento = 0.2
    quinzePorCento = 0.15
    dezPorCento = 0.1
    cincoPorCento = 0.05

    if salario >= 0.00 and salario <= 280.00:
        salarioRounder = round(salario, 2)
        salarioSemAjuste = str(salarioRounder)

        novoSalario = salario + (salario * vintePorCento)
        salarioRound = round(novoSalario, 2)
        strSalario = str(salarioRound)

        valorAumento = novoSalario - salario
        valorRound = round(valorAumento, 2)
        valorAjustado = str(valorRound)

        salarios.label_verificar.setText("Salário - R$ " + salarioSemAjuste)
        salarios.label_verificar_2.setText("Aumento de 20%")
        salarios.label_verificar_3.setText("Valor do aumento - R$ " + valorAjustado)
        salarios.label_verificar_4.setText("O novo salário - R$ " + strSalario)
    
    elif salario > 280.00 and salario <= 700.00:
        salarioRounder = round(salario, 2)
        salarioSemAjuste = str(salarioRounder)

        novoSalario = salario + (salario * quinzePorCento)
        salarioRound = round(novoSalario, 2)
        strSalario = str(salarioRound)

        valorAumento = novoSalario - salario
        valorRound = round(valorAumento, 2)
        valorAjustado = str(valorRound)

        salarios.label_verificar.setText("Salário - R$ " + salarioSemAjuste)
        salarios.label_verificar_2.setText("Aumento de 15%")
        salarios.label_verificar_3.setText("Valor do aumento - R$ " + valorAjustado)
        salarios.label_verificar_4.setText("O novo salário - R$ " + strSalario)
    
    elif salario > 700.00 and salario <= 1500.00:
        salarioRounder = round(salario, 2)
        salarioSemAjuste = str(salarioRounder)

        novoSalario = salario + (salario * dezPorCento)
        salarioRound = round(novoSalario, 2)
        strSalario = str(salarioRound)

        valorAumento = novoSalario - salario
        valorRound = round(valorAumento, 2)
        valorAjustado = str(valorRound)

        salarios.label_verificar.setText("Salário - R$ " + salario)
        salarios.label_verificar_2.setText("Aumento de 20%")
        salarios.label_verificar_3.setText("Valor do aumento - R$ " + valorAjustado)
        salarios.label_verificar_4.setText("O novo salário - R$ " + strSalario)

    elif salario > 1500.00:
        salarioRounder = round(salario, 2)
        salarioSemAjuste = str(salarioRounder)

        novoSalario = salario + (salario * cincoPorCento)
        salarioRound = round(novoSalario, 2)
        strSalario = str(salarioRound)

        valorAumento = novoSalario - salario
        valorRound = round(valorAumento, 2)
        valorAjustado = str(valorRound)

        salarios.label_verificar.setText("Salário - " + salarioSemAjuste)
        salarios.label_verificar_2.setText("Aumento de 20%")
        salarios.label_verificar_3.setText("Valor do aumento - " + valorAjustado)
        salarios.label_verificar_4.setText("O novo salário - R$ " + strSalario)


app = QtWidgets.QApplication([])
salarios = uic.loadUi("decisao-11.ui")
salarios.pb_verificar.clicked.connect(verificacao)
salarios.show()
app.exec()