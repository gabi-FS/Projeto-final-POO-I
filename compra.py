#Trabalho POO I - Compra
#Gabriela Furtado da Silveira

from datetime import datetime
from medicamento import Medicamento
from estoque import Estoque
from time import sleep

class Compra():
    def __init__(self, cpf):
        self.cpf = cpf
        self.itens = {}
        self.formaPgt = 'Dinheiro'
        self.dinheiro = 0.0
        self.total = 0.0
        self.troco = 0.0

    def adicionar_item(self, produto, numero):
        if produto.quantidade >= numero:
            if isinstance(produto, Medicamento):
                if produto.receita == True:
                    print('O medicamento inserido só pode ser vendido sob prescrição médica.')
                    receita = input('Digite S para confirmar a apresentação da receita: ').upper()
                    if receita == 'S':
                        self.itens[produto.nome] = numero, produto.preco
                    else:
                        print('Item cancelado.\n')
                        return
            else:        
                self.itens[produto.nome] = numero, produto.preco
        elif produto.quantidade == 0:
            print('Nenhuma unidade em estoque.\n')
            return
        else:
            print('Nº de unidades inserido não disponível em estoque.')
            resp = input(f'{produto.quantidade} unidades em estoque. Deseja adicionar todas à compra? (S/N) ').upper().strip()
            while resp not in 'SN':
                print('Insira S para "sim" e N para "não".')
                resp = input(f'{produto.quantidade} unidades em estoque. Deseja adicionar todas à compra? (S/N) ').upper().strip()
            if resp == 'S':
                self.itens[produto.nome] = produto.quantidade, produto.preco
            else: 
                print('Item cancelado.\n')
                return
        produto.quantidade = produto.quantidade - self.itens[produto.nome][0]
        print('Item adicionado!\n')
        
    def total_compra(self):
        self.total = 0
        for x in self.itens.values():
            self.total += x[0]*x[1]
        return self.total
    def pagamento(self, formaPgt, dinheiro):
        self.formaPgt = formaPgt
        self.troco = (dinheiro - self.total)
        if formaPgt == 'Cartão de crédito':
            vezes = input('Deseja parcelar em quantas vezes (1 a 5)? ')
            while vezes not in '12345':
                print('Valor inválido; insira um número de 1 a 5!')
                vezes = input('Deseja parcelar em quantas vezes (1 a 5)? ')
            vezes = int(vezes)
            print(f'{vezes}X de R${self.total/vezes:.2f}.')
            sleep(1)
            print('Processando pagamento...')
            sleep(1)
            print()
        elif formaPgt == 'Dinheiro':
            while dinheiro - self.total < 0:
                print(f'Valor insuficiente. O total da compra foi de R${self.total:.2f}.')
                dinheiro = float(input('Valor recebido do cliente:'))
            print(f'Troco de {dinheiro - self.total}.')
        else:
            sleep(1)
            print('Processando pagamento...')
            sleep(1)
        print('Pagamento efetuado com sucesso!')
        self.dinheiro = dinheiro
        
    def nota_fiscal(self):
        data = datetime.now()
        print('{:%d-%m-%Y %H:%M:%S}'.format(data))
        sleep(0.5)
        print(f'CPF consumidor: {self.cpf}')
        sleep(0.5)
        print('           CUPOM FISCAL')
        for n, x in self.itens.items():
            print(f'{n:10}....{x[0]:2}un......R${x[1]:>4.2f}')
            sleep(0.5)
        print(' '*20, '-'*13)
        sleep(0.5)
        print(f'Total', '.'*19, f'R${self.total:>5.2f}')
        sleep(0.5)
        print(f'{self.formaPgt:26}R${self.dinheiro:>5.2f}')
        sleep(0.5)
        if self.formaPgt == 'Dinheiro':
            t = 'Troco'
            print(f'{t:21}R${self.troco:>5.2f}')

            