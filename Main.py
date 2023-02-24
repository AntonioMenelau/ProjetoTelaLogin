# ---------------------------------------------------------------------------------------
#
#   Projeto Tela Login v1.0
#   Criado por: Antonio Menelau da Silva Neto
#   Projeto desenvolvido usando python QTDesign e SQLite 
#
# ---------------------------------------------------------------------------------------


# importando a tela Login
from Files.CoreQt import *
import Login

# inicializando a Tela
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Login = Login.Login()
    sys.exit(app.exec_())