import math

#definir as variaveis:
base = float(input("Base do retangulo: "))
altura = float(input('Altura do retangulo:'))

#Definir as funções:
def area(base, altura):
    return base * altura

def perimetro(base, altura):
    return 2 * (base + altura)

def diagonal(base, altura):
    return math.sqrt((base**2) + altura**2)

#Chamadas daas funções:
print("---------------------------------------------------------------")
print("Area = {:.2f}".format(area(base, altura)))
print("Perimetro = {:.2f}".format(perimetro(base, altura)))
print("Diagonal = {:.2f}".format(diagonal(base, altura)))
print("===============================================================")

#########################################################################

#definir as variaveis:
base = float(input("Base do retangulo: "))
altura = float(input('Altura do retangulo:'))

#Definir as funções:
area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt((base**2) + altura**2)

#Chamadas daas funções:
print("--------------------------------------------------------------")
print(f"Area = {area:.2f}")
print(f"Perimetro =  {perimetro:.2f}")
print(f"Diagonal = {diagonal:.2f}")
print("===============================================================")
