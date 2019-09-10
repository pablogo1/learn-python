# Listas 1

calificaciones = [10, 9, 8, 10, 9, 8, 6]
promedio = 0
numero_elementos = 0
suma = 0

for calificacion in calificaciones:
    numero_elementos = numero_elementos + 1
    suma = suma + calificacion

promedio = suma / numero_elementos

print("Promedio: ", promedio)

# Usando while
numero_elementos = len(calificaciones)
indice = 0
suma = 0

while indice < numero_elementos:
    suma = suma + calificaciones[indice]
    indice = indice + 1

promedio = suma / numero_elementos

print("Promedio: ", promedio)

# Python tiene integradas funciones muy utiles que nos ayudan a hacer esto
# más rápido!! :D
# Usando len y sum
suma = sum(calificaciones)
numero_elementos = len(calificaciones)

promedio = suma / numero_elementos

print("Promedio: ", promedio)

