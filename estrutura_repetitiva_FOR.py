#for i in range(0, 10, 2):
#  print(i)


N = int(input("Quantos numeros serão digitados? "))

soma = 0
for i in range(0, N):
    x = int(input("Digite um numero: "))
    soma = soma + x

    print("SOMA = ",soma)