import sqlite3

def criar_tabela_usuario(conexao):

    cursor = conexao.cursor()

    sql =  """
        CREATE TABLE IF NOT EXISTS usuario (
            nome TEXT  NOT NULL, 
            login TEXT  NOT NULL,
            senha TEXT  NOT NULL
        );
    
    """
    cursor.execute(sql)

def inserir_usuario(conexao):
    cursor = conexao.cursor()
    sql = """
        INSERT INTO usuario VALUES(
            'Matheus Borges',
            'borges',
            'b123'
        );
    
    """
    cursor.execute(sql)
    conexao.commit()

##############################################

conexao = sqlite3.connect("banco.sqlite")

#criar_tabela_usuario(conexao)
inserir_usuario(conexao)
conexao.close()