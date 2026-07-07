from cadastro import cadastrar_usuarios, listar_usuarios, apagar_todos_usuarios, apagar_usuario

def menu():
    while True:
        print("Escolha entre \n 1) Cadastrar usuário \n 2) Listar usuário \n 3) Apagar um usuário \n 4) Apagar todos os usuários \n 5) Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            senha = input("Digite a senha do usuário: ")
            telefone = input("Digite o telefone do usuário: ")
            cadastrar_usuarios(nome, senha, telefone)

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