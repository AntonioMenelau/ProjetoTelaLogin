from sqlite3 import connect

banco = ""

def pegarDados(tabela=str, dados=str):
    """
    Ele acessa o banco de dados e retorna uma lista

    Args:
        tabela (str, optional): Digite o nome da Tabela, Defaults to str.
        dados (str, optional): informe qual dado quer ser acessado, Defaults to list.
    """
    
    bd = connect(f"{banco}")
    cursor = bd.cursor()
    listaDeDados = []
    for ron in cursor.execute(f"Select {dados} from {tabela};"):
        listaDeDados.append(ron)
    bd.close()
    
    return listaDeDados


def inserirDados(tabela=str, dados=str):
    """
    Ele adiciona novos dados para o banco de dados, e retorna um print avisando que foi adicionado.

    Args:
        tabela (str, optional): A tabela em que sera inserido os valores, Defaults to str.
        tipos (str, optional): Uma linha de texto, apontando onde cada valor vai ser inserido, Defaults to str.
            ex: tipos = " column1, column2, column3, ..."
        dados (str, optional): Os dados em ordem que sera inserida, Defaults to str.
            ex: dados = " null, 'teste', 'teste2', ..."
    """
    
    bd = connect(f"{banco}")
    cursor = bd.cursor()
    cursor.execute(f"INSERT INTO {tabela} VALUES ({dados});")
    bd.commit()
    bd.close()
    
    return print("adicionado com Sucesso")