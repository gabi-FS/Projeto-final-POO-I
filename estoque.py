#Trabalho POO I - Estoque
#Gabriela Furtado da Silveira

from produto import Produto
from cosmetico import Cosmetico
from medicamento import Medicamento

class Estoque():
    def __init__(self):
        self.lista_produtos = []
    def novo_produto(self, nome, preco, quantia, selec):
        if selec != 'S':
            prod = Produto(nome, preco, quantia)
            return prod
        else:
            categoria = input('Digite M para medicamento e C para cosmético: ').upper()
            while categoria not in 'MC':
                categoria = input('Digite M para medicamento e C para cosmético: ')
            if categoria == 'M':
                lab = input('Laboratório do medicamento: ').lower().strip()
                presc = False
                receita = input('Necessita apresentar receita para a compra? (S/N) ').upper()
                while receita not in ('SN'):
                    print('Insira S em caso positivo e N em caso negativo.')
                    receita = input('Necessita apresentar receita para a compra? (S/N) ').upper()
                if receita == 'S':
                    presc = True
                remedio = Medicamento(nome, preco, quantia, lab, presc)
                return remedio
            else:
                marca = input('Informe a marca do cosmético: ').lower().strip()
                cosmet = Cosmetico(nome, preco, quantia, marca)
                return cosmet
     
    def cadastrar_produto(self, produto):
        self.lista_produtos.append(produto)
        print('\nProduto cadastrado e adicionado ao estoque!')
    def excluir_produto(self, nome):
        busca = False
        for produto in self.lista_produtos:
            if produto.nome == nome.lower().strip():
                self.lista_produtos.remove(produto)
                print(f'{produto.nome} removido do sistema.')
                busca = True
        if busca != True:
            print(f'Produto não encontrado.')
    def info_produto(self, nome):
        busca = False
        for produto in self.lista_produtos:
            if produto.nome == nome.lower().strip():
                produto.exibir_dados()
                busca = True
        if busca != True:
            print(f'Produto não encontrado.')
    def repor_estoque(self, nome, novas_unidades):
        busca = False
        for produto in self.lista_produtos:
            if produto.nome == nome.lower().strip():
                produto.quantidade += int(novas_unidades)
                busca = True
                print('Novas unidades adicionadas!')
        if busca != True:
            print(f'Produto não encontrado.')   
    def achar_produto(self, nome):
        for produto in self.lista_produtos:
            if produto.nome == nome.lower().strip():
                return produto
        print(f'Produto não encontrado.\n') 
        return 