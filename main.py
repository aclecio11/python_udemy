a: float #casting
b: int
a = 5.32
b= int (a)
print("b =",b)
print(f"b = {b}")


x = 1.456789999
idade = 20
salario = 5800.5
altura = 1.63
genero = "F"
nome = "Maria Silva"

print("X = {:.2f}".format(x))
print(f"Idade = {idade}")
print(f"Salario = {salario:.2f}")
print(f"Altura = {altura:.2f}")
print(f"Genero = {genero}")
print(f"Nome = {nome}")

print("%s tem %d anos" % (nome, idade))
print(f"{nome} tem {idade} anos")

print("A funcionária %s, tem %d anos, sexo %s, altura %.2f e recebe $%.2f de salário" %(nome, idade, genero, altura, salario))
print(f"A funcionaria {nome}, tem {idade} anos de idade,sexo {genero}, altura {altura:.2f} e recebe ${salario:.2f} de salario")