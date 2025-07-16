# Sistema de E-commerce Básico (Linha de Comando)

Um projeto simples em Python para simular as funcionalidades básicas de um sistema de e-commerce, tudo executado no terminal (linha de comando).

## 📖 Sobre o Projeto

Este projeto foi criado como um exercício de programação para praticar conceitos fundamentais de Python, como loops, condicionais, funções e manipulação de estruturas de dados (dicionários e listas).

O sistema simula um fluxo de e-commerce, começando com a autenticação do usuário (login/cadastro) e seguindo para um menu onde o usuário pode interagir com funcionalidades de uma loja virtual. Atualmente, os dados de usuários são armazenados em memória, o que significa que são apagados toda vez que o programa é encerrado.

---

## ✨ Funcionalidades

### ✅ Implementadas
* **Sistema de Cadastro:** Permite que novos usuários criem uma conta.
* **Sistema de Login:** Autentica usuários já cadastrados.
* **Menu Principal Interativo:** Navegação baseada nas escolhas do usuário.
* **Menu Condicional:** A opção de "Organização dos produtos" só aparece para usuários administradores (ex: usuário 'admin').

### 🚧 Planejadas
* **Visualização de Produtos:** Listar todos os produtos disponíveis.
* **Carrinho de Compras:** Adicionar, remover e visualizar itens no carrinho.
* **Finalização de Pedido:** Simular o processo de checkout.
* **Pagamento e Entrega:** Funções para simular os processos de pagamento e entrega.
* **Gerenciamento de Produtos:** Um painel para o administrador adicionar ou remover produtos do "estoque".

---

## 🛠️ Estrutura do Código

O código está dividido nas seguintes seções principais:

1.  **Armazenamento de Dados:** Um dicionário chamado `usuarios` é usado para guardar os logins e senhas em memória.
2.  **Loop de Autenticação:** O primeiro `while True` que cuida do login e do cadastro de usuários. O programa só avança após um login bem-sucedido.
3.  **Definição de Funções:** Cada opção do menu principal (Procurar Produtos, Carrinho, etc.) tem sua própria função. Isso mantém o código organizado e fácil de expandir.
4.  **Loop do Menu Principal:** O segundo `while True` que aparece após o login, permitindo que o usuário escolha o que deseja fazer.

---

## 💡 Próximos Passos e Melhorias

* Implementar a lógica interna de cada uma das funções planejadas.
* Criar uma estrutura de dados para `produtos` (sugestão: uma lista de dicionários).
* Criar uma estrutura de dados para o `carrinho` de cada usuário.
* **Persistência de Dados:** Modificar o sistema para salvar os dados de usuários e produtos em um arquivo (como `.json` ou `.csv`), para que não se percam ao fechar o programa.
* **Orientação a Objetos:** Refatorar o código para usar Classes (ex: `class Usuario`, `class Produto`), tornando-o mais robusto e escalável.
