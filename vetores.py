N = int

N = int(input("Quantos números serão digitados? "))

vet = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input("Digite um número: "))

print()
print("NÚMEROS DIGITADOS: ")
for i in range(0,N):
    print(f"{vet[i]:.1f}")