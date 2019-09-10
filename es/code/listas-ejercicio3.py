# Listas 3 - Histograma

datos = [10, 8, 5, 2, 5, 1, 0, 7, 40]

i = 1
for d in datos:
    print(i, "|", end=" ")
    for j in range(1, d + 1):
        print("+", end="")
    # print(" (", d, ")", end="")
    print("")
    i = i + 1
