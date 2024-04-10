from Roupa import Roupa

class Camisa(Roupa):
    __Cam_Tipo = None
    __Cam_Botoes = None
    __Cam_Bolsos = None
    __Cam_Gola = None

    def __init__(self):
        super().__init__()
        self.__Cam_Tipo = ""
        self.__Cam_Botoes = 0
        self.__Cam_Bolsos = 0
        self.__Cam_Gola = True

    def Leitura(self):
        self.__Cam_Tipo = input("Qual o tipo da camisa? ")
        self.__Cam_Botoes = int(input("Qual o número de botões da camisa? "))
        self.__Cam_Bolsos = int(input("Quantos bolsos tem a camisa? "))
        self.__Cam_Gola = input("Tem gola? ") == "True"
        super().Leitura()
        
    def toString(self):
        str = ""
        str += "\nImpressão das Camisas"
        str += f"\nTipo de camisa={self.__Cam_Tipo}"
        str += f"\nQuantidade de botões={self.__Cam_Botoes}"
        str += f"\nQuantidade de bolsos={self.__Cam_Bolsos}"
        str += f"\nTem gola={self.__Cam_Gola}"
        str += "\n"
        str += super().toString()
        return str
        
    def __del__(self):
        super().__del__()
        print("Passei no destrutor da classe Camisa...")
       
