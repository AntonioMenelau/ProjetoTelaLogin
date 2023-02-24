from sqlite3 import connect

banco = ""

def pegarDados(tabela=str, dados=str):
    """
    Ele acessa o banco de dados e retorna uma lista

    Args:
        tabela (Digite o noem da Tabela): Defaults to str.
        banco (Digite o caminho do banco de dados):  Defaults to str.
        dados (informe qual dado quer ser acessado): Defaults to list.
    """
    
    bd = connect(f"{banco}")
    cursor = bd.cursor()
    listaDeDados = []
    for ron in cursor.execute(f"Select {dados} from {tabela};"):
        listaDeDados.append(ron)
    
    return listaDeDados