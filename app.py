def procurar_produtos():
    print("\n\t--- Procurar Produtos ---")
    print("\t(Função ainda não implementada)")

def organizar_carrinho():
    print("\n\t--- Organizar Carrinho de Compras ---")
    print("\t(Função ainda não implementada)")

def realizar_pedido():
    print("\n\t--- Realizar Pedido ---")
    print("\t(Função ainda não implementada)")

def processo_pagamento():
    print("\n\t--- Processo de Pagamento ---")
    print("\t(Função ainda não implementada)")

def processo_entrega():
    print("\n\t--- Processo de Entrega ---")
    print("\t(Função ainda não implementada)")

def organizacao_produtos_admin():
    print("\n\t--- Organização dos Produtos (Admin) ---")
    print("\t(Função ainda não implementada)")


usuarios = {'admin': '1234'} # Usuário teste base

while True:
    print("\n\tBem-vindo(a)!")

    opcao = int(input("\t1 - Login\n\t2 - Cadastro\n\t=>"))

    if opcao == 1:
        user = input("\tLogin: ")
        senha = input("\tSenha: ")

        if user in usuarios and usuarios[user] == senha:
            print(f"\n\tBem-vindo(a). {user}")
            break
        else:
            print("\n\t[ERRO] Login ou senha inválidos. Tente novamente.")

    elif opcao == 2:
        print("\n\t--- Tela de Cadastro ---")
        novo_user = input("\tDigite o nome de usuãrio desejado: ")

        if novo_user in usuarios:
            print("\n\t[ERRO] Este nome de usuário já existe. Escolha outro.")
        else:
            nova_senha = input("\tDigite a senha desejada: ")
            usuarios[novo_user] = nova_senha
            print(f"\n\tUsuário '{novo_user}' cadastrado com sucesso!")
            print("\tAgora você pode fazer o login.")

    else:
        print("\n\t[ERRO] Digite uma opção válida (1 ou 2).")


while True:
    print("\n\tO que deseja fazer?")
    print("\t" + "="*25)
    print("\t1 - Procurar produtos")
    print("\t2 - Organizar carrinho de compras")
    print("\t3 - Realizar pedido")
    print("\t4 - Processo de pagamento")
    print("\t5 - Processo de entrega")
    # A opção 6 deve ser apenas para administradores
    if user == 'admin': # Exemplo: só mostra a opção 6 se o usuário logado for 'admin'
        print("\t6 - Organização dos produtos")
    print("\t0 - Deslogar e Sair")
    print("\t" + "="*25)

    try:
        escolha = int(input("\tDigite sua escolha: "))
    except ValueError:
        print("\n\t[ERRO] Por favor, digite um número.")
        continue

    if escolha == 1:
        procurar_produtos()
    elif escolha == 2:
        organizar_carrinho()
    elif escolha == 3:
        realizar_pedido()
    elif escolha == 4:
        processo_pagamento()
    elif escolha == 5:
        processo_entrega()
    elif escolha == 6 and user == 'admin': # Garante que só o admin acesse
        organizacao_produtos_admin()
    elif escolha == 0:
        print(f"\n\tAté logo, {user}!")
        break # Sai do menu principal e encerra o programa
    else:
        print("\n\t[ERRO] Opção inválida. Tente novamente.")
