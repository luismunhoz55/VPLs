import sys
from Camisa import Camisa

##################################################

## Questão 13: Qual o código necessário para criar o programa principal?
cam=Camisa()
cam.Leitura()
cam.Calcula_Total()
print(cam.toString())
cam.__del__()
del(cam)

## Questão 14: Qual o comando que encerra o programa principal?
sys.exit(0)

##################################################
