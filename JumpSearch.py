import math

def pesquisa_por_salto(lista, elemento):
    n = len(lista)
    salto = int(math.sqrt(n))  
    anterior = 0

    while lista[min(salto, n) - 1] < elemento:
        anterior = salto
        salto += int(math.sqrt(n))
        if anterior >= n:
            return -1  

    for i in range(anterior, min(salto, n)):
        if lista[i] == elemento:
            return i

    return -1  

#Exemplo:
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

elemento = 15

resultado = pesquisa_por_salto(lista, elemento)

if resultado != -1:
    print(f"Elemento {elemento} encontrado no índice {resultado}.")
else:
    print(f"Elemento {elemento} não encontrado na lista.")
