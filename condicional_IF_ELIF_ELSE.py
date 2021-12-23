hora: int
hora = int(input("Digite uma hora do dia:"))

if hora < 12:   #se = if
    print("Bom dia!")
elif hora < 18:    #elif = se nao se
    print("Boa tarde")
else:    #else = se nao
    print("Boa noite")


