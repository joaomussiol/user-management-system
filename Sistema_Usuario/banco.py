import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "usuarios.db")

conexao = sqlite3.connect(DB_PATH)
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