from cadastro import cadastrar_usuarios, listar_usuarios, apagar_todos_usuarios, apagar_usuario

def solicitar_cadastro():
    while True:
        nome = input("Digite o nome do usuário:")
        if nome.strip() == "":
            print("Nome não pode ser vazio! Tente novamente.")

        elif any(caractere.isdigit() for caractere in nome):
            print("Nome não pode conter números! Tente novamente.")

        else:
            break
    while True:
        senha = input("Digite a senha do usuário:")
        if len(senha) <8:
            print("Senha deve ter no mínimo 8 caracteres! Tente novamente.")
        elif not any(c.isupper() for c in senha):
            print("Senha deve conter pelo menos uma letra maiúscula! Tente novamente.")
        elif not any(c.islower() for c in senha):
            print("Senha deve conter pelo menos uma letra minúcula! Tente novamente.")
        elif not any(c.isdigit() for c in senha):
            print("Senha deve conter pelo menos um número! Tente novamente.")
        elif not any(c in "!@#$%¨&*()-_=+[]{}|;:,.<>?/~`" for c in senha):
            print("Senha deve ter pelo menos um caractere especial! Tente novamente.")
        else:
            break
        
    while True:
        telefone = input("digite o telefone do usuário:")
        telefone_limpo = telefone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
        if telefone_limpo.strip() == "":
            print("Telefone não pode ser vazio! Tente novamente.")

        elif not telefone_limpo.isdigit():
            print("Telefone deve conter apenas números! Tente novamente.")
        
        elif len(telefone_limpo) <8 or len(telefone_limpo) >11:
            print("Telefone deve ter entre 8 e 11 dígitos! Tente novamente.")

        else:
            break
        
    cadastrar_usuarios(nome, senha, telefone_limpo)

def menu():
    while True:
        print("Escolha entre \n 1) Cadastrar usuário \n 2) Listar usuário \n 3) Apagar um usuário \n 4) Apagar todos os usuários \n 5) Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            solicitar_cadastro()

        elif opcao == "2":
            listar_usuarios()

        elif opcao == "3":
            usuario_id = input("Digite o ID do usuário a ser apagado: ")
            apagar_usuario(usuario_id)

        elif opcao == "4":
            apagar_todos_usuarios()

        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()