#Trabalho POO I - main
#Gabriela Furtado da Silveira

from compra import Compra
from estoque import Estoque
from produto import Produto
from time import sleep

estoque1 = Estoque()
  
while True:
    print('+'*40)
    print('{:^40}'.format('Sistema Fármacia Padrão'))
    print('{:^40}'.format('...MENU...'))
    print('[1] Cadastrar um novo produto')
    print('[2] Excluir produto do sistema')
    print('[3] Consultar dados de um produto')
    print('[4] Reposição de produto')
    print('[5] Nova compra')
    print('[6] Sair')
    resp = input('Selecione uma opção: ')
    while resp not in '123456':
        print('Insira uma opção (1 a 6).')
        resp = input('Selecione uma opção: ')
    print('+'*40)
    if resp == '6':
        break
    elif resp == '1':
        print()
        nome = input('Nome do produto: ').lower().strip()
        preco = float(input('Preço do produto: '))
        quantia = int(input('Nº de unidades: '))
        selec = input('É um cosmético ou medicamento? (S/N) ').upper()
        estoque1.cadastrar_produto(estoque1.novo_produto(nome, preco, quantia, selec))
        sleep(1)
        print()

    elif resp == '2':
        print()
        estoque1.excluir_produto(input('Informe o nome do produto que deseja excluir: '))
        sleep(1)
        print()

    elif resp == '3':
        print()
        estoque1.info_produto(input('Informe o nome do produto que deseja buscar: '))
        sleep(2)
        print()

    elif resp == '4':
        print()
        nome, un = input('Informe o nome do produto e a o nº de unidades a ser adicionado (separe com espaço): ').split()
        estoque1.repor_estoque(nome, un)
        sleep(1)
        print()

    else:
        print()
        cpf = int(input('Informe o CPF do cliente: '))
        compra1 = Compra(cpf)
        while True:
            nome = input('Insira o nome do produto: ')
            quant = input('Nº de unidades: ')
            prod = estoque1.achar_produto(nome)
            if isinstance(prod, Produto):
                compra1.adicionar_item(prod, int(quant))
                s = input('Deseja inserir mais algum produto? (S/N) ').upper()
                while s not in ('SN'):
                    print('Insira S em caso positivo e N em caso negativo.\n')
                    s = input('Deseja inserir mais algum produto? (S/N) ').upper()
                print()
                if s == 'N':
                    break
        print('--'*30)
        print(f'TOTAL: R${compra1.total_compra():.2f}\n')
        print(f'[1] Dinheiro \n[2] Cartão de débito \n[3] Cartão de crédito')
        formaPgt = input('Insira a forma de pagamento: ')
        while formaPgt not in '123':
            print('Essa não é uma opção válida! Insira uma opção (1 a 3).')
            formaPgt = input('Insira a forma de pagamento: ')
        if formaPgt == '1':
            valor = float(input('Valor recebido do cliente: '))
            compra1.pagamento('Dinheiro', valor)
        elif formaPgt == '2':
            compra1.pagamento('Cartão de débito', compra1.total_compra())
        else:
            compra1.pagamento('Cartão de crédito', compra1.total_compra())
        print('--'*30)
        nota = input('Deseja emitir o cupom fiscal? (S/N) ').upper()
        if nota == 'S':
            print()
            compra1.nota_fiscal()
            sleep(2)
        print('\nCompra finalizada!')
        sleep(1)
        print('+'*40)        