from PyQt5 import uic, QtWidgets

def verificacao():

    nota1 = float(notas.lineEdit_nota1.text())
    nota2 = float(notas.lineEdit_nota2.text())

    media = (nota1 + nota2) / 2

    if media >= 0.0 and media < 4.0:
        nota1Round = round(nota1, 2)
        strNota1 = str(nota1Round)

        nota2Round = round(nota2, 2)
        strNota2 = str(nota2Round)

        mediaRound = round(media, 2)
        strMedia = str(mediaRound)

        notas.label_verificar.setText(f'Nota 1 - {strNota1} e Nota 2 - {strNota2}')
        notas.label_verificar_2.setText(f'Média - {strMedia}')
        notas.label_verificar_3.setText(f'Reprovado - Conceito E')

    elif media >= 4.0 and media < 6.0:
        nota1Round = round(nota1, 2)
        strNota1 = str(nota1Round)

        nota2Round = round(nota2, 2)
        strNota2 = str(nota2Round)

        mediaRound = round(media, 2)
        strMedia = str(mediaRound)

        notas.label_verificar.setText(f'Nota 1 - {strNota1} e Nota 2 - {strNota2}')
        notas.label_verificar_2.setText(f'Média - {strMedia}')
        notas.label_verificar_3.setText(f'Reprovado - Conceito D')

    elif media >= 6.0 and media < 7.5:
        nota1Round = round(nota1, 2)
        strNota1 = str(nota1Round)

        nota2Round = round(nota2, 2)
        strNota2 = str(nota2Round)

        mediaRound = round(media, 2)
        strMedia = str(mediaRound)

        notas.label_verificar.setText(f'Nota 1 - {strNota1} e Nota 2 - {strNota2}')
        notas.label_verificar_2.setText(f'Média - {strMedia}')
        notas.label_verificar_3.setText(f'Aprovado - Conceito C')

    elif media >= 7.5 and media < 9.0:
        nota1Round = round(nota1, 2)
        strNota1 = str(nota1Round)

        nota2Round = round(nota2, 2)
        strNota2 = str(nota2Round)

        mediaRound = round(media, 2)
        strMedia = str(mediaRound)

        notas.label_verificar.setText(f'Nota 1 - {strNota1} e Nota 2 - {strNota2}')
        notas.label_verificar_2.setText(f'Média - {strMedia}')
        notas.label_verificar_3.setText(f'Aprovado - Conceito B')

    elif media >= 9.0 and media <= 10.0:
        nota1Round = round(nota1, 2)
        strNota1 = str(nota1Round)

        nota2Round = round(nota2, 2)
        strNota2 = str(nota2Round)

        mediaRound = round(media, 2)
        strMedia = str(mediaRound)

        notas.label_verificar.setText(f'Nota 1 - {strNota1} e Nota 2 - {strNota2}')
        notas.label_verificar_2.setText(f'Média - {strMedia}')
        notas.label_verificar_3.setText(f'Aprovado - Conceito A')


app = QtWidgets.QApplication([])
notas = uic.loadUi("decisao-14.ui")
notas.pb_verificar.clicked.connect(verificacao)
notas.show()
app.exec()