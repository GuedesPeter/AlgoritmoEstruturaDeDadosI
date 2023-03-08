from time import sleep

class Produto:
    def __init__(self,nome,preco,qtde):
        self.__nome = nome
        self.__preco = preco
        self.__qtde = qtde

    def nome_produto(self):
        return print(self.__nome)

    def preco_produto(self):
        return print(self.__preco)

    def qtde_produto(self):
        return print(self.__qtde)

    def __str__(self):
        print(f'NOME: {self.__nome} / PREÇO: {self.__preco} / QTDE.: {self.__qtde}')



produto1 = Produto('coca-cola','R$8,49',5)
produto2 = Produto('Pepsi','R$8,05',10)
produto3 = Produto('Fanta','R$7,89',2)


#produto1.nome_produto()
#produto1.preco_produto()
#produto1.qtde_produto()


lista_Produtos = [produto1,produto2,produto3]

def todos_produtos():
    for ind,produto in enumerate(lista_Produtos):
        sleep(0.5)
        print(ind,produto.__str__())


def ler_produto():
    posicao = int(input('Digite a posição do produto: '))
    sleep(1)
    lista_Produtos[posicao].__str__()

def remover_produto():
    todos_produtos()
    posicao = int(input('Digite a posição do produto a REMOVER: '))
    lista_Produtos.pop(posicao)
    sleep(1)
    print('PRODUTO REMOVIDO')

#todos_produtos()
#ler_produto(2)
#remover_produto(1)


while True:
    print('''
    1 - TODOS OS PRODUTOS
    2 - LER UM PRODUTO
    3 - REMOVER UM PRODUTO
    4 - SAIR
    
    ''')
    escolha = int(input('ESCOLHA: '))

    if escolha < 1 and escolha >= 5 :
        print('ESCOLHA UMA OPÇÃO VÁLIDA!')
    if escolha == 1:
        todos_produtos()
    if escolha == 2:
        ler_produto()
    if escolha == 3:
        remover_produto()
    if escolha == 4:
        print('Finalizando... ... ...')
        sleep(2)
        break

#finalizado