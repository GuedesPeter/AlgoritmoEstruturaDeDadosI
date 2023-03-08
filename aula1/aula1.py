'''
Construir um algoritmo que contenha 3 listas, cada lista contendo:
Nomes de produtos
Preços de cada produto
Quantidades de cada produto
Construir uma função para imprimir um dos produtos da lista e uma
função para retirar um dos produtos das listas. As funções devem receber
um parâmetro que será usado para acessar a posição dos itens das listas
que serão impressos ou retirados.
'''


nomeProduto = ['Coca-Cola','Pepsi','Fanta','Polar','Amstel','Budwiser']
precoProduto = ['R$9,05','R$8,79','R$8,15','R$4,75','R$4,89','R$5,29']
qtdeProduto = [3,4,5,6,7,8]

def listar_produtos():
    for ind,prod in enumerate(nomeProduto):
        print(f'{ind} - {prod}')


#listar_produtos()


def imprime_produto(indice):
    print(nomeProduto[indice])


#imprime_produto(0)

def remove_produto(indice):
    nomeProduto.pop(indice)
    print(nomeProduto)

#remove_produto(0)

'''
def imprime_produto():
    listar_produtos()
    print('Escolha a posição do item que quer visualizar: ')
    escolha = int(input())
    print( nomeProduto[escolha])

#imprime_produto()

def remove_produto():
    listar_produtos()
    print('Escolha a posição do produto a ser REMOVIDO:')
    escolha = int(input())
    nomeProduto.pop(escolha)
    print(nomeProduto)


#remove_produto()

'''
