import sqlite3
conexao = sqlite3.connect("usuarios.db")

cursor = conexao.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               senha TEXT NOT NULL,
               telefone TEXT NOT NULL)
""")

conexao.commit()
conexao.close()