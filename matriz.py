M = int(input("Quantas linhas vai ter a matriz? "))
N  = int(input("Quantas colunas vai ter a matriz?"))

mat: [[int]] = [[0 for x in range(N) ] for x in range(M)]
#fazer uma estrutura "para" para poder percorrer os elementos da matriz
for i in range(0, M):
    for j in range(0, N):
        mat[i][j] = int(input(f"Elemento[{i}, {j}]: "))

print()
print("Matriz digitada: ")
for i in range(0, M):
    for j in range(0, N):
        print(f"{mat[i][j]} ", end="")  #Esse end é para quebrar a linha
    print() #Esse print é referente ao primeiro for