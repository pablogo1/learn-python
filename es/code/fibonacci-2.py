# Obtener el n-número de fibonacci
# Usando ciclos

def fib(n):
    x1 = 0
    x2 = 1
    contador = 3
    xn = 0
    i = 0

    while contador <= n:
        print("iteracion: ", i)
        i = i + 1
        xn = x1 + x2
        x1 = x2
        x2 = xn
        contador = contador + 1
        
    if n == 1: 
        xn = x1
    if n == 2:
        xn = x2
    
    return xn

print (fib(10))