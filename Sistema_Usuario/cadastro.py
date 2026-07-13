import sqlite3
import os
import bcrypt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "usuarios.db")

def cadastrar_usuarios(nome, senha, telefone):
    senha_hash = bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt())
    
    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()

    cursor.execute("""
                INSERT INTO usuarios (nome, senha, telefone)
                VALUES(?, ?, ?)
                """, (nome, senha_hash, telefone))
    
    conexao.commit()
    conexao.close()

def listar_usuarios():
    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor. fetchall()

    conexao.close()
    return usuarios

def apagar_todos_usuarios():
    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()

    cursor.execute ("DELETE FROM usuarios")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='usuarios'")

    conexao.commit()
    conexao.close()

def apagar_usuario(id):
    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    
    conexao.commit()
    conexao.close()
    