from cadastro import cadastrar_usuarios, listar_usuarios, apagar_todos_usuarios, apagar_usuario

def solicitar_cadastro(): # solicita os dados do usuário e valida as entradas. Opção 1 do menu.
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

def exibir_usuarios(): # lista os usuários cadastrados. Opção 2 do menu.
    usuarios = listar_usuarios()
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("Usuários cadastrados:")
        for usuario in usuarios:
            print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Telefone: {usuario[3]}")

def solicitar_apagar_usuario(): # solicita o ID do usuário que deseja apagar. Opção 3 do menu.
    listar_usuarios()
    input_usuario_id = input("Digite o ID do usuário que deseja apagar:")
    if input_usuario_id.isdigit() and input_usuario_id.strip():
        usuario_id = int(input_usuario_id)
        apagar_usuario(usuario_id)
    else:
        print("ID inválido. Por favor, insira um número válido.")

def solicitar_apagar_todos_usuarios(): # solicita confirmação para apagar todos os usuários. Opção 4 do menu.
    confirmacao = input("Tem certeza que deseja apagar todos os usuários? (s/n):")
    if confirmacao.lower().strip() == "s":
        apagar_todos_usuarios()
    else:
        print("Operação cancelada.")

def menu(): # exibe o menu principal e lida com as opções do usuário.
    while True:
        print("Escolha entre \n 1) Cadastrar usuário \n 2) Listar usuário \n 3) Apagar um usuário \n 4) Apagar todos os usuários \n 5) Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            solicitar_cadastro()

        elif opcao == "2":
            exibir_usuarios()

        elif opcao == "3":
            solicitar_apagar_usuario()

        elif opcao == "4":
            solicitar_apagar_todos_usuarios()

        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()