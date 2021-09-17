#Trabalho POO I - Produto
#Gabriela Furtado da Silveira

class Produto():
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def exibir_dados(self):
        print(f'Dados de {self.nome}:')
        print(f' + Preço: {self.preco:.2f}')
        print(f' + Quantidade em estoque: {self.quantidade}')
    
        
