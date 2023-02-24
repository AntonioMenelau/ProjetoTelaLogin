# ---------------------------------------------------------------------------------------
#
#   Projeto Tela Login v1.0
#   Criado por: Antonio Menelau da Silva Neto
#   Projeto desenvolvido usando python QTDesign e SQLite 
#
# ---------------------------------------------------------------------------------------


# importando todas as bibliotecas necessarias para aplicação
from Files.CoreQt import *


# GUI Tela Login
class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        # importando a tela Login
        self.telaLogin = loadUi("UI\\Login\\TelaLogin.ui", self)
        
        # configurando a janela como translucida e tirando a moldura da aplicação 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.telaLogin.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        # importando os componenes do UI
        self.nome = self.findChild(QLineEdit, "inputNome")
        self.senha = self.findChild(QLineEdit, "inputSenha")
        self.entrar  = self.findChild(QPushButton, "btnEntrar")
        self.lembrar = self.findChild(QCheckBox, "checkLembrar")
        self.cadastro = self.findChild(QPushButton, "btnCadastro")
        self.sair = self.findChild(QPushButton, "btnFechar")
        
        # Funções dos Botões
        self.entrar.clicked.connect(lambda: print("botao de entrar clicado"))
        self.cadastro.clicked.connect(lambda: print("botao de cadastro clicado"))
        self.sair.clicked.connect(lambda: self.telaLogin.close())
        
        # mostrando a tela login
        self.telaLogin.show()


