#Trabalho POO I - Cosmético(Produto)
#Gabriela Furtado da Silveira
from produto import Produto

class Cosmetico(Produto):
    def __init__(self, nome, preco, quantidade, marca):
        super().__init__(nome, preco, quantidade)
        self.marca = marca
    def exibir_dados(self):
        print(f'Dados de {self.nome} (cosmético):')
        print(f' + Preço: {self.preco:.2f}')
        print(f' + Quantidade em estoque: {self.quantidade}')
        print(f' + Marca: {self.marca}')
        