from PySide6.QtWidgets import QApplication, QPushButton

#Aplicação:
app = QApplication()

#Botão
botao = QPushButton("Clique aqui")
botao.setStyleSheet('font-size: 20px; color: red') 
botao.show()#Exibir

#Execução da aplicação
app.exec()

#9:17 parei aqui