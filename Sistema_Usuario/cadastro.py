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

    for usuario in usuarios:
        print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Telefone: {usuario[3]}")

    conexao.close()

def apagar_todos_usuarios():
    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()

    cursor.execute ("DELETE FROM usuarios")

    conexao.commit()
    conexao.close()

def apagar_usuario(id):
    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    
    conexao.commit()
    conexao.close()
    