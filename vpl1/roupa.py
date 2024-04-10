##################################################

class Roupa(object):
    ## Questão 01: Qual o código que define as características da classe base Roupa?
    __Roupa_Marca = None
    __Roupa_Cor = None
    __Roupa_Tam = None
    __Roupa_Quant = None
    __Roupa_Preco = None
    __Total_Roupa = None
    
    ## Questão 02: Qual o código que define o construtor que inicia as características da classe Roupa?
    ##             (Os valores iniciais encontram-se no diagrama de classes)
    def __init__(self):
        self.__Roupa_Marca = ""
        self.__Roupa_Cor = ""
        self.__Roupa_Tam = 0
        self.__Roupa_Quant = 0
        self.__Roupa_Preco = 0.0
        self.__Total_Roupa = 0.0
    
    def Leitura(self):
        ## Questão 03: Qual o código necessário para efetuar a leitura das características da classe Roupa?
        self.__Roupa_Marca=input("Digite a marca da roupa: ")
        self.__Roupa_Cor=input("Digite a cor da roupa: ")
        self.__Roupa_Tam = int(input("Digite o tamanho da roupa: "))
        self.__Roupa_Quant=int(input("Digite a quantidade: "))
        self.__Roupa_Preco=float(input("Digite o preço: "))
        
    def Calcula_Total(self):
        ## Questão 04: Qual o código necessário para calcular a despesa total da compra das peças de roupa?
        self.__Total_Roupa = self.__Roupa_Quant * self.__Roupa_Preco

    def toString(self):
        ## Questão 05: Qual o código necessário para imprimir em uma string todas as características da classe Roupa?
        Str = "\n"
        Str += "Impressão das Roupas\n"
        Str += f"Marca da roupa=%s\n" % self.__Roupa_Marca
        Str += f"Cor da roupa={self.__Roupa_Cor}\n"
        Str += f"Tamanho da roupa={self.__Roupa_Tam}\n"
        Str += f"Quantidade de roupas={self.__Roupa_Quant}\n"
        Str += "Preço da peça de roupa=%5.2f\n" % self.__Roupa_Preco
        Str += f"Total=%5.2f\n" % self.__Total_Roupa
        return Str
    
    ## Questão 06: Qual o código que define o destrutor da classe Roupa?
    ##             O destrutor deve escrever na tela:
    ##             Passei no destrutor da classe Roupa...
    def __del__(self):
        print("Passei no destrutor da classe Roupa...")

##################################################
