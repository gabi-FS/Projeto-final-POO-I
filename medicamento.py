#Trabalho POO I - Medicamento(Produto)
#Gabriela Furtado da Silveira
from produto import Produto

class Medicamento(Produto):
    def __init__(self, nome, preco, quantidade, laboratorio, receita):
        super().__init__(nome, preco, quantidade)
        self.laboratorio = laboratorio
        self.receita = receita
    def exibir_dados(self):
        print(f'Dados de {self.nome} (medicamento):')
        print(f' + Preço: {self.preco:.2f}')
        print(f' + Quantidade em estoque: {self.quantidade}')
        print(f' + Laboratório: {self.laboratorio}')
        if self.receita == True:
            print('  ** Venda mediante apresentação de receita médica.')
