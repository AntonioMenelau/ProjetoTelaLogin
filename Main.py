# ---------------------------------------------------------------------------------------
#
#   Projeto Tela Login v1.0
#   Criado por: Antonio Menelau da Silva Neto
#   Projeto desenvolvido usando python QTDesign e SQLite 
#
# ---------------------------------------------------------------------------------------


# importando todas as bibliotecas necessarias para aplicação
from Files.CoreQt import *

# função responsavel pela troca de janelas 
def abrirJanela(janela=1):
    """Responsavel pela troca de janelas

    Args:
        janela (int, optional, defaut=1): numero inteiro que representa qual janela abrir.
        
        janelas:
            1 - Login\n
            2 - Cadastro
    """
    
    # importando as janelas
    import Login
    import Cadastro
    
    # seleção das janelas
    if janela == 1:
        Login = Login.Login()
    if janela == 2:
        Cadastro = Cadastro.Cadastro()
        

# inicializando a Tela
if __name__ == "__main__":
    app = QApplication(sys.argv)
    abrirJanela()
    sys.exit(app.exec_())