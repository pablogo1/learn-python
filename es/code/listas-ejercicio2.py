# Listas 2

calificaciones = [10, 9, 8, 10, 9, 8, 6]
contador = 1

for calificacion in calificaciones:
    print(contador, end=" ")
    for i in range(1, calificacion + 1):
        print("+", end="")

    print("")
    contador = contador + 1
