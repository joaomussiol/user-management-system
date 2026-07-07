import sqlite3

def cadastrar_usuarios(nome, senha, telefone):
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()

    cursor.execute("""
                INSERT INTO usuarios (nome, senha, telefone)
                VALUES(?, ?, ?)
                """, (nome, senha, telefone))
    
    conexao.commit()
    conexao.close()

cadastrar_usuarios("João", "1234", "48999999999")
