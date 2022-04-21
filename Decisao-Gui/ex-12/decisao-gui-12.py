import math
from PyQt5 import uic, QtWidgets

def verificacao():

    valorHora = int(salario.lineEdit.text())
    quantidadeHora = int(salario.lineEdit_2.text())

    salarioBruto = valorHora * quantidadeHora

    ir = 0.05
    inss = 0.1
    fgts = 0.11

    if salarioBruto >= 0.00 and salarioBruto <= 900.00:    

        strValorHora = str(valorHora)
        strQuantidadeHora = str(quantidadeHora)

        salarioRound = round(salarioBruto, 2)
        strSalario = str(salarioRound)

        impostoInss = (salarioBruto * inss)
        inssRound = round(impostoInss, 2)
        strInss = str(inssRound)

        contribuiFgts = (salarioBruto * fgts)
        fgtsRound = round(contribuiFgts, 2)
        strFgts = str(fgtsRound)

        totalDescontos = (impostoRenda + impostoInss)
        totalDescontosRound = round(totalDescontos, 2)
        strTotalDescontos = str(totalDescontosRound)

        salarioLiquido = (salarioBruto - impostoRenda - impostoInss)
        salarioLiquidoRound = round(salarioLiquido, 2)
        strSalarioLiquido = str(salarioLiquidoRound)

        salario.label_verificar.setText(f'Salário Bruto: ({strValorHora} * {strQuantidadeHora})        : R$ {strSalario}')
        salario.label_verificar_2.setText("(-) IR (5%)               : R$ ISENTO")
        salario.label_verificar_3.setText("(-) INSS (10%)           : R$ " + strInss)
        salario.label_verificar_4.setText("FGTS (11%)               : R$ " + strFgts)
        salario.label_verificar_5.setText("Total de descontos      : R$ " + strTotalDescontos)
        salario.label_verificar_6.setText("Salário Líquido           : R$ " + strSalarioLiquido)

    elif salarioBruto > 900.00 and salarioBruto <= 1500.00:    

        strValorHora = str(valorHora)
        strQuantidadeHora = str(quantidadeHora)

        salarioRound = round(salarioBruto, 2)
        strSalario = str(salarioRound)

        impostoRenda = (salarioBruto * ir)
        irRound = round(impostoRenda, 2)
        strIr = str(irRound)

        impostoInss = (salarioBruto * inss)
        inssRound = round(impostoInss, 2)
        strInss = str(inssRound)

        contribuiFgts = (salarioBruto * fgts)
        fgtsRound = round(contribuiFgts, 2)
        strFgts = str(fgtsRound)

        totalDescontos = (impostoRenda + impostoInss)
        totalDescontosRound = round(totalDescontos, 2)
        strTotalDescontos = str(totalDescontosRound)

        salarioLiquido = (salarioBruto - impostoRenda - impostoInss)
        salarioLiquidoRound = round(salarioLiquido, 2)
        strSalarioLiquido = str(salarioLiquidoRound)

        salario.label_verificar.setText(f'Salário Bruto: ({strValorHora} * {strQuantidadeHora})        : R$ {strSalario}')
        salario.label_verificar_2.setText("(-) IR (5%)               : R$ " + strIr)
        salario.label_verificar_3.setText("(-) INSS (10%)           : R$ " + strInss)
        salario.label_verificar_4.setText("FGTS (11%)               : R$ " + strFgts)
        salario.label_verificar_5.setText("Total de descontos      : R$ " + strTotalDescontos)
        salario.label_verificar_6.setText("Salário Líquido           : R$ " + strSalarioLiquido)

    elif salarioBruto > 1500.00 and salarioBruto <= 2500.00:

        strValorHora = str(valorHora)
        strQuantidadeHora = str(quantidadeHora)

        salarioRound = round(salarioBruto, 2)
        strSalario = str(salarioRound)

        impostoRenda = (salarioBruto * (ir + 0.05))
        irRound = round(impostoRenda, 2)
        strIr = str(irRound)

        impostoInss = (salarioBruto * inss)
        inssRound = round(impostoInss, 2)
        strInss = str(inssRound)

        contribuiFgts = (salarioBruto * fgts)
        fgtsRound = round(contribuiFgts, 2)
        strFgts = str(fgtsRound)

        totalDescontos = (impostoRenda + impostoInss)
        totalDescontosRound = round(totalDescontos, 2)
        strTotalDescontos = str(totalDescontosRound)

        salarioLiquido = (salarioBruto - impostoRenda - impostoInss)
        salarioLiquidoRound = round(salarioLiquido, 2)
        strSalarioLiquido = str(salarioLiquidoRound)

        salario.label_verificar.setText(f'Salário Bruto: ({strValorHora} * {strQuantidadeHora})        : R$ {strSalario}')
        salario.label_verificar_2.setText("(-) IR (5%)               : R$ " + strIr)
        salario.label_verificar_3.setText("(-) INSS (10%)           : R$ " + strInss)
        salario.label_verificar_4.setText("FGTS (11%)               : R$ " + strFgts)
        salario.label_verificar_5.setText("Total de descontos      : R$ " + strTotalDescontos)
        salario.label_verificar_6.setText("Salário Líquido           : R$ " + strSalarioLiquido)

    elif salarioBruto > 2500.00:

        strValorHora = str(valorHora)
        strQuantidadeHora = str(quantidadeHora)

        salarioRound = round(salarioBruto, 2)
        strSalario = str(salarioRound)

        impostoRenda = (salarioBruto * (ir + 0.15))
        irRound = round(impostoRenda, 2)
        strIr = str(irRound)

        impostoInss = (salarioBruto * inss)
        inssRound = round(impostoInss, 2)
        strInss = str(inssRound)

        contribuiFgts = (salarioBruto * fgts)
        fgtsRound = round(contribuiFgts, 2)
        strFgts = str(fgtsRound)

        totalDescontos = (impostoRenda + impostoInss)
        totalDescontosRound = round(totalDescontos, 2)
        strTotalDescontos = str(totalDescontosRound)

        salarioLiquido = (salarioBruto - impostoRenda - impostoInss)
        salarioLiquidoRound = round(salarioLiquido, 2)
        strSalarioLiquido = str(salarioLiquidoRound)

        salario.label_verificar.setText(f'Salário Bruto: ({strValorHora} * {strQuantidadeHora})        : R$ {strSalario}')
        salario.label_verificar_2.setText("(-) IR (5%)               : R$ " + strIr)
        salario.label_verificar_3.setText("(-) INSS (10%)           : R$ " + strInss)
        salario.label_verificar_4.setText("FGTS (11%)               : R$ " + strFgts)
        salario.label_verificar_5.setText("Total de descontos      : R$ " + strTotalDescontos)
        salario.label_verificar_6.setText("Salário Líquido           : R$ " + strSalarioLiquido)

        
app = QtWidgets.QApplication([])
salario = uic.loadUi("decisao-12.ui")
salario.pb_verificar.clicked.connect(verificacao)
salario.show()
app.exec()