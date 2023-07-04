# ---------------------------------------------------------------------------------------
#
#   Projeto Tela Login v1.0
#   Criado por: Antonio Menelau da Silva Neto
#   Projeto desenvolvido usando python QTDesign e SQLite 
#
# ---------------------------------------------------------------------------------------


# importando todas as bibliotecas necessarias
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QCheckBox
from PyQt5.QtCore import pyqtSignal
from PyQt5.uic import loadUi
import Login.Files.FilesTelaLogin
import Login.Cadastro as cadastro

# GUI tela Login
class Login(QMainWindow):
    login_success = pyqtSignal()
    def __init__(self):
        super(Login, self).__init__()
        # importando a tela Login
        self.telaLogin = loadUi(r"Login\UI\Login\TelaLogin.ui", self)
        
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
        self.entrar.clicked.connect(lambda: self.Logar())
        self.cadastro.clicked.connect(lambda: self.telaCadastro())
        self.sair.clicked.connect(lambda: self.telaLogin.close())
        
        # mostrando a tela login
        self.telaLogin.show()

    # função que valida se o nome ou a senha estao cadastrados
    def Logar(self):
        # conectando o banco de dados 
        import Funcoes.getDATA as dt
        dt.banco= "Banco de Dados\\BD.sqlite"
        dados = dt.pegarDados(tabela="Cadastrados", dados="*")
        
        nome = self.nome.text()
        senha = f"{self.nome.text()} {self.senha.text()}"
        
        x = False
        y = False
        for cadastrado in dados:
            if cadastrado[1] == nome:
                x=True
                if f"{cadastrado[1]} {cadastrado[2]}" == senha:
                    y=True
                break
        
        if x == True:
            if y == True:
                print("Acesso concedido")
                self.login_success.emit()
                self.telaLogin.close()
            else:
                print("nome encontrado")
                print("Acesso negado")
        else:
            print("nome não cadastrado")
    
    def telaCadastro(self):
        self.telaLogin.close()
        cadastro.Cadastro()
   
            
def initLogin():
    app = QApplication(sys.argv)
    login = Login()
    success = [False]

    def on_login_success():
        success[0] = True

    login.login_success.connect(on_login_success)

    app.exec_()

    return 1 if success[0] else 0
