# ---------------------------------------------------------------------------------------
#
#   Projeto Tela Login v1.0
#   Criado por: Antonio Menelau da Silva Neto
#   Projeto desenvolvido usando python QTDesign e SQLite 
#
# ---------------------------------------------------------------------------------------


# importando todas as bibliotecas necessarias
from Files.CoreQt import *

# GUI tela Cadastro
class Cadastro(QMainWindow):
    def __init__(self):
        super(Cadastro, self).__init__()
        # importando a tela Login
        self.TelaCadastro = loadUi("UI\\Cadastro\\TelaCadastro.ui", self)
        
        # configurando a janela como translucida e tirando a moldura da aplicação 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.TelaCadastro.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
        # importando os componentes UI
        self.nome = self.findChild(QLineEdit, "inputNome")
        self.senha = self.findChild(QLineEdit, "inputSenha")
        self.confirmSenha = self.findChild(QLineEdit, "inputConfirmSenha")
        self.cadastro  = self.findChild(QPushButton, "btnCadastro")
        self.entrar = self.findChild(QPushButton, "btnEntrar")
        self.sair = self.findChild(QPushButton, "btnFechar")
        
        # Funçoes nos botoes
        self.sair.clicked.connect(lambda: self.TelaCadastro.close())
        self.cadastro.clicked.connect(lambda: self.register())
        self.entrar.clicked.connect(lambda: self.telaLogin())
        
        # mostrando a tela Cadastro
        self.TelaCadastro.show()
    
    # função que validade o usuario e se a senha foi digitada corretamente, e registra o usuario novo 
    def register(self):
        # conectando o banco de dados 
        import Funcoes.getDATA as dt
        dt.banco= "Banco de Dados\\BD.sqlite"
        dados = dt.pegarDados(tabela="Cadastrados", dados="*")
        
        nome = self.nome.text()
        senha = self.senha.text()
        senhaConfirm = self.confirmSenha.text()
        
        
        # verificar se nao existe um usuario igual
        uex = True  # --> nao existe
        for c in dados:
            if c[1] == nome:
                uex = False  # --> existe
        
        
        # verificar se a senha digitada foi identica na confirm
        sex = False
        if senha == senhaConfirm:
            sex = True
        
        # cadastrar o novo usuario
        if uex + sex == 2:
            dt.inserirDados(tabela="Cadastrados", dados=f"null, '{nome}', '{senha}'")
        else:
            print("Erro no cadastro")
        

    def telaLogin(self):
        # fechando a tela Cadastro
        self.TelaCadastro.close()
        
        # abrindo a tela Login
        from Main import abrirJanela
        abrirJanela(janela=1)        