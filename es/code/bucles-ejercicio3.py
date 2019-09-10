# Usar ciclos para preguntar al usuario que ingrese un número entero entre 0 y 10. 
# Si el valor ingreado está fuera de rango preguntar de nuevo.

# valor = -1
# while valor < 0 or valor > 10:
#     valor = int(input('Introduzca un valor entre 0 y 10: '))

# print('Gracias')

while True:
    valor = int(input('Introduzca un valor entre 0 y 10: '))

    if valor >= 0 and valor <= 10:
        break

print ('Gracias')