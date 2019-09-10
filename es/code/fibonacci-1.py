# Obtener el n-número de fibonacci
# Usando recursión

def fib(n):
    print ('Llamando fib(', n, ')')
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-2) + fib(n-1)

print (fib(10))