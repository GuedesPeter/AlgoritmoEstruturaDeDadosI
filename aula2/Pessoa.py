
class Pessoa():
    def __init__(self,nome,idadePessoa):
        self.nome = nome
        self.idade = idadePessoa
        self.fone = input("Digite o telefone: ")
        #self.imprimir() - RECURSIVIDADE 

    def imprimir(self):
        print(f'{self.nome} - {self.idade} - {self.fone}')
    