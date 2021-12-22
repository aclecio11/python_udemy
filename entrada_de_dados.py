nome1: str ; nome2: str
salario1: float ; salario2: float
idade1: int ; idade2: int
sexo1: str ; sexo2: str

nome1 = input("Digite o nome da primeira pessoa: ")
salario1 = float(input("Digite o salario da primeira pessoa: "))

nome2 = input("Digite o nome da segunda pessoa: ")
salario2 = float(input("Digite o salario da segunda pessoa: "))

idade1 = int(input("Digite a idade da primeira pessoa: "))
sexo1 = input("Digite um genero sexual da primeira pessoa(F/M): ")

idade2 = int(input("Digite a idade da segunda pessoa: "))
sexo2 = input("Digite um genero sexual da segunda pessoa(F/M): ")
print("----------------------------------------------------------------------")

print(f"Nome da primeira pessoa: {nome1}")
print(f"Salario da primeira pessoa: {salario1:.2f}")

print(f"Nome da segunda pessoa: {nome2}")
print(f"Salario da segunda pessoa: {salario2:.2f}")

print(f"Sexo1: {sexo1}")
print(f"Idade1: {idade1}")

print(f"Sexo2: {sexo2}")
print(f"Idade2: {idade2}")