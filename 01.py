import sys
from PySide6.QtWidgets import QApplication, QMainWindow

# Criar a aplicação
app = QApplication(sys.argv)

#Criar janela principal
janela = QMainWindow()
janela.setWindowTitle("Minha Primeiro Janela no Pyside6")
janela.resize(800, 600)
janela.show()

# iniciar o loop de eventos (A aplicação fica viva aqui!)
sys.exit(app.exec_())
