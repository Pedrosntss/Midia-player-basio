import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QCheckBox)

from PySide6.QtCore import Qt
class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widgets Básicos")
        self.resize(420, 500)

        # Layout vertical para empilhar os widgets
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Qlabel
        titulo = QLabel("Cadastro de Aluno")
        titulo.setAlignment(Qt.AlignCenter)
        #Estilo inline (subset de CSS)
        titulo.setStyleSheet("font-size:18px; font-weight: bold; color: #00b4d8; padding: 8px;")
        layout.addWidget(titulo)

        # QLineEdit
        self.campo_nome = QLineEdit()
        self.campo_nome.setPlaceholderText("Digite seu nome completo")
        layout.addWidget(QLabel("Nome:"))
        layout.addWidget(self.campo_nome)


        # LineEdit com o modo senha (Esconder os caracteres)
        self.campo_senha = QLineEdit()
        self.campo_senha.setPlaceholderText("Senha...")
        self.campo_senha.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(QLabel("Senha:"))
        layout.addWidget(self.campo_senha)

        #QTextEdit
        layout.addWidget(QLabel("Observações"))
        self.area_texto = QTextEdit()
        self.area_texto.setPlaceholderText("Digite as informações aqui...")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Widget()
    window.show()
    sys.exit(app.exec_())
