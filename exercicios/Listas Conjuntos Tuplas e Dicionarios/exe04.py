livraria = {
"Python para Iniciantes": {"autor": "Guido van Rossum", "ano": 2010, "estoque": 5},
"Algoritmos em C": {"autor": "Robert Sedgewick", "ano": 2016, "estoque": 3},
"Estruturas de Dados": {"autor": "Thomas Cormen", "ano": 2018, "estoque": 7}
}

def exibirLivros(livro_estoque:dict):
    for livro, info_livro in livro_estoque.items():
        autor = info_livro["autor"]
        ano = info_livro["ano"]
        estoque = info_livro['estoque']
        print(f"{livro}:Autor: {autor} - Ano: {ano} - Estoque: {estoque}")

def buscarLivroporTitulo(livro_estoque:dict, titulo):
    print(f'\n--- Buscando por "{titulo}" ---')
    
    if (titulo in livro_estoque):
        info_livro = livro_estoque[titulo]
        autor = info_livro["autor"]
        ano = info_livro["ano"]
        estoque = info_livro["estoque"]
        print(f"{titulo} - Autor: {autor} - Ano: {ano} - Estoque: {estoque}")
        return info_livro
    else:
        print(f'Livro "{titulo}" não encontrado.')
        return None

def adicionarLivro(livro_estoque:dict,titulo, autor, ano, quantidade):
    if (titulo in livro_estoque):
        print(f'\nERRO: O livro "{titulo}" já existe no estoque. Use a função de atualização.')
    else:
        novo_livro = {
            "autor": autor,
            "ano": ano,
            "estoque": quantidade
        }
        livro_estoque[titulo] = novo_livro
        print(f'\nLivro "{titulo}" adicionado ao estoque!')
        
def atualizarLivro(livro_estoque:dict, titulo, quantidade):
    if (titulo in livro_estoque):
        livro_estoque[titulo]["estoque"] = quantidade
        print(f'\nEstoque do livro "{titulo}" atualizado para {quantidade}!')
    else:
        print(f'\nERRO: Livro "{livro_estoque}" não encontrado para atualização.')
        
def removerLivro(livro_estoque:dict, titulo_remover):
    if (titulo_remover in livro_estoque):
        livro_estoque.pop(titulo_remover)
        print(f'\nLivro "{titulo_remover}" removido do estoque!')
    else:
        print(f'\nERRO: Livro "{titulo_remover}" não encontrado para remoção.')
def main():
    print()
    exibirLivros(livraria)
    print()
    buscarLivroporTitulo(livraria, "Algoritmos em C")
    print()
    adicionarLivro(livraria, "Os manos", "Matheus", 2025,10)
    print()
    exibirLivros(livraria)
    print()
    atualizarLivro(livraria, "Estruturas de Dados",15)
    print()
    removerLivro(livraria, "Python para Iniciantes")

main()