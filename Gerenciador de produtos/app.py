from Produto import Produto

produtos = []

def main():
    while True:
        option = input("\n\nSelecione uma opção:\n1) Cadastro de produto\n2) Listar Produtos\n3) Atualizar produto\n4) Excluir Produto\n0) Encerrar o programa\n")
        if option == "1": 
            novoProduto()
        elif option == "2":
            listarProdutos()
        elif option == "3":
            atualizaProduto()
        elif option == "4":
            excluirProduto()
        elif option == "0":
            return
        else:
            print("Comando inválido")

def novoProduto():
    while (True):
        nome = input("Nome: ")
        preco = input("Preço: ")
        categoria = input("Categoria: ")
        fabricante = input("Fabricante: ")
        validade = input("Validade: ")
    
        produto = Produto(nome, preco, categoria, fabricante, validade)
        produtos.append(produto)
        print("\nProduto cadastrado com sucesso!\n")
        
        continuarCadastrando = input("Continuar cadastrando produtos? S/N")
        if (continuarCadastrando.upper() != "S"):
            return
        
def listarProdutos():
    for produto in produtos:
        print("---\nNome: ", produto.get_nome(), "\nPreço: ", produto.get_preco(), "\nValidade: ", produto.get_validade(), "\nFabricante: ", produto.get_fabricante(), "\nCategoria: ", produto.get_categoria())

def atualizaProduto():
    indexProduto = buscaProduto()
    if indexProduto != -1:
        while True:
            print("\nNome: ", produtos[indexProduto].get_nome(), "\nPreço: ", produtos[indexProduto].get_preco(), "\nValidade: ", produtos[indexProduto].get_validade(), "\nFabricante: ", produtos[indexProduto].get_fabricante(), "\nCategoria: ", produtos[indexProduto].get_categoria())
            opcao = input("Qual informação deseja alterar? (nome, preço, validade, fabricante, categoria)")
            if opcao.upper() == 'NOME':
                produtos[indexProduto].set_nome(input("Informe o nome: "))
            if opcao.upper() == 'PREÇO':
                produtos[indexProduto].set_preco(input("Informe o preço: "))
            if opcao.upper() == 'VALIDADE':
                produtos[indexProduto].set_validade(input("Informe a validade: "))
            if opcao.upper() == 'FABRICANTE':
                produtos[indexProduto].set_fabricante(input("Informe o fabricante: "))
            if opcao.upper() == 'CATEGORIA':
                produtos[indexProduto].set_categoria(input("Informe o categoria: "))

            continuarEditando = input("Continuar editando produto? S/N\n")
            if (continuarEditando.upper() != "S"):
                return

def excluirProduto():
    indexProduto = buscaProduto()
    if indexProduto != -1:
        confirmacao = input("Tem certeza que deseja excluir? S/N\n")
        if confirmacao.upper() == "S":
            produtos.pop(indexProduto)
            print("\nProduto excluído com sucesso!\n")

def buscaProduto():
    produtoBusca = input("Busque o produto pelo nome: ")
    index = -1
    for produto in produtos:
        if produto.get_nome() == produtoBusca:
            index = produtos.index(produto)
    return index

main()