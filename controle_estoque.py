# -------------------------------------------
# Aluno: Kayo Víctor Oliveira da Silva Viana
# Data: 20/06/2025
# Versão: 1.0
# -------------------------------------------

# ------------------------------------------------------------
# Desenvolvendo um Sistema de Controle de Estoque com Python
# Soluções para Gerenciamento em uma Loja de Eletrônicos
# ------------------------------------------------------------

# Escolhi uma lista de dicionários para o estoque.
# É uma estrutura simples e flexível para começar. Cada dicionário guardará as informações de um produto.
estoque = []

# --- Cores para o Terminal (Não requerido, mas eu quis adicionar para dar um charme especial :D ) ---
class Cores:
    RESET = "\033[0m"
    VERMELHO = "\033[31m"
    VERDE = "\033[32m"
    AMARELO = "\033[33m"
    AZUL = "\033[34m"
    CIANO = "\033[36m"

# --- Funções Auxiliares de Interface para exibir mensagens no terminal (também não requerido, mas útil e evita repetição de código) ---
def print_sucesso(mensagem):
    # Imprime uma mensagem de sucesso em verde.
    print(f"{Cores.VERDE}{mensagem}{Cores.RESET}")

def print_erro(mensagem):
    # Imprime uma mensagem de erro em vermelho.
    print(f"{Cores.VERMELHO}{mensagem}{Cores.RESET}")

def print_info(mensagem):
    # Imprime uma mensagem de informação em ciano.
    print(f"{Cores.CIANO}{mensagem}{Cores.RESET}")

def print_titulo(titulo):
    """Imprime um título formatado."""
    print(f"\n{Cores.AMARELO}--- {titulo} ---{Cores.RESET}")


def adicionar_produto():
    """
    Adiciona um novo produto ao estoque.
    Realiza validações para garantir que os dados sejam inseridos corretamente.
    """
    print_titulo("Adicionar Novo Produto")

    # 1. Coleta e valida o nome do produto
    nome = input("Nome do Produto: ").strip().title()
    if not nome:
        print_erro("O nome do produto não pode ser vazio. Operação cancelada.")
        return

    # Verifica se o produto já existe (ignorando maiúsculas/minúsculas)
    for produto in estoque:
        if produto['nome'].lower() == nome.lower():
            print_erro(f"O produto '{nome}' já está cadastrado.")
            return

    # 2. Coleta e valida o preço
    try:
        preco = float(input("Preço (R$): "))
        if preco <= 0:
            print_erro("O preço deve ser um valor positivo. Operação cancelada.")
            return
    except ValueError:
        print_erro("Preço inválido. Use apenas números (ex: 49.99).")
        return

    # 3. Coleta e valida a quantidade
    try:
        quantidade = int(input("Quantidade em Estoque: "))
        if quantidade < 0:
            print_erro("A quantidade não pode ser negativa. Operação cancelada.")
            return
    except ValueError:
        print_erro("Quantidade inválida. Use apenas números inteiros.")
        return

    # 4. Adiciona o produto ao estoque
    novo_produto = {
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    }
    estoque.append(novo_produto)
    print_sucesso(f"\nProduto '{nome}' adicionado com sucesso!")


def atualizar_produto():
    # Atualiza as informações de um produto existente.
    print_titulo("Atualizar Produto")
    nome_produto = input("Nome do produto a ser atualizado: ").strip()
    for produto in estoque:
      if produto['nome'].lower() == nome_produto.lower():
        try:
          novo_preco = float(input("Novo preço (R$): ").replace(',', '.'))
          if novo_preco < 0:
            print_erro("O preço não pode ser negativo.")
            return
        except ValueError:
          print_erro("Preço inválido. Utilize apenas números.")
          return

        try:
          nova_quantidade = int(input("Nova quantidade em estoque: "))
          if nova_quantidade < 0:
            print_erro("A quantidade não pode ser negativa.")
            return
        except ValueError:
          print_erro("Quantidade inválida. Utilize apenas números inteiros.")
          return

        produto['preco'] = novo_preco
        produto['quantidade'] = nova_quantidade
        print_sucesso(f"Produto '{nome_produto}' atualizado com sucesso!")
        return
    print_erro("Produto não encontrado no estoque.")
    pass

def excluir_produto():
    # Remove um produto do estoque.
    print_titulo("Excluir Produto")
    nome_produto = input("Nome do produto a ser excluído: ").strip()
    for i, produto in enumerate(estoque):
      if produto['nome'].lower() == nome_produto.lower():
        confirmacao = input(f"Tem certeza que deseja excluir '{produto['nome']}'? (s/n): ").strip().lower()
        if confirmacao == 's':
          del estoque[i]
          print_sucesso(f"Produto '{nome_produto}' removido do estoque com sucesso!")
        else:
          print_info("Exclusão cancelada pelo usuário.")
        return
    print_erro("Produto não encontrado no estoque.")
    pass

def visualizar_estoque():
    # Exibe todos os produtos em estoque.
    print_titulo("Estoque Atual")
    if not estoque:
      print_info("O estoque está vazio.")
      return

    print(f"{'Nome':<25} {'Preço (R$)':<12} {'Quantidade':<10}")
    print("-" * 50)
    for produto in estoque:
      nome = produto['nome']
      preco = f"R$ {produto['preco']:.2f}"
      quantidade = produto['quantidade']
      print(f"{nome:<25} {preco:<12} {quantidade:<10}")
    pass

def main():
    # Função principal que executa o menu do sistema.
    while True:
        print_titulo("Sistema de Controle de Estoque")
        print(f"{Cores.AZUL}1.{Cores.RESET} Adicionar Produto")
        print(f"{Cores.AZUL}2.{Cores.RESET} Atualizar Produto")
        print(f"{Cores.AZUL}3.{Cores.RESET} Excluir Produto")
        print(f"{Cores.AZUL}4.{Cores.RESET} Visualizar Estoque")
        print(f"{Cores.AZUL}5.{Cores.RESET} Sair")

        try:
            opcao = int(input(f"\n{Cores.CIANO}Escolha uma opção:{Cores.RESET} "))

            if opcao == 1:
                adicionar_produto()
            elif opcao == 2:
                atualizar_produto()
            elif opcao == 3:
                excluir_produto()
            elif opcao == 4:
                visualizar_estoque()
            elif opcao == 5:
                print_sucesso("\nFechando o sistema. Boas vendas!")
                break
            else:
                print_erro("Opção inválida. Por favor, escolha um número do menu.")
        except ValueError:
            print_erro("Entrada inválida. Por favor, insira um número.")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
