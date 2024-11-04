def pesquisa_fibonacci(lista, elemento):
    n = len(lista)

    fib_m2 = 0  
    fib_m1 = 1  
    fib_m = fib_m2 + fib_m1 

    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    offset = -1

    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)

        if lista[i] < elemento:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif lista[i] > elemento:
            fib_m = fib_m2
            fib_m1 -= fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i 

    if fib_m1 and offset + 1 < n and lista[offset + 1] == elemento:
        return offset + 1

    return -1  

#Exemplo:
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

elemento = 9

resultado = pesquisa_fibonacci(lista, elemento)

if resultado != -1:
    print(f"Elemento {elemento} encontrado no índice {resultado}.")
else:
    print(f"Elemento {elemento} não encontrado na lista.")

