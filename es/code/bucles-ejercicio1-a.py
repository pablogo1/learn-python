# Bucles 1
# Inciso a

contador = 1
while contador <= 5:
    print(contador, end=" ")
    for i in range(1, contador + 1):
        print("*", end="")

    print("")
    contador = contador + 1

# Inciso b
print("")
contador = 5
while contador >= 1:
    print(contador, end=" ")
    for i in range(1, contador + 1):
        print("*", end="")

    print("")
    contador = contador - 1

# Triangulo
print("")
altura = 5
contador = 0

for i in range(1, altura + 1):
    num_plus = i * 2 - 1 
    espacios = altura - i
    for j in range(1, espacios + 1):
        print(" ", end=" ")
    for z in range(1, num_plus + 1):
        print("+", end=" ")
    print("")

# Diamante
print("")
altura = 5
contador = 0

for i in range(1, altura + 1):
    num_plus = i * 2 - 1
    espacios = altura - i
    for j in range(1, espacios + 1):
        print(" ", end=" ")
    for z in range(1, num_plus + 1):
        print("+", end=" ")
    print("")

for i in range(altura - 1, 0, -1):
    num_plus = i * 2 - 1
    espacios = altura - i
    for j in range(1, espacios + 1):
        print(" ", end=" ")
    for z in range(1, num_plus + 1):
        print("+", end=" ")
    print("")
