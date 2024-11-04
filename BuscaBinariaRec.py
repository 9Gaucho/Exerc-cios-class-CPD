def busca_binaria_recursiva(lista, elemento, esquerda, direita):
    if esquerda > direita:
        return -1 

    meio = (esquerda + direita) // 2
    if lista[meio] == elemento:
        return meio
    elif lista[meio] < elemento:
        return busca_binaria_recursiva(lista, elemento, meio + 1, direita)
    else:
        return busca_binaria_recursiva(lista, elemento, esquerda, meio - 1)

# Exemplo:
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

elemento = 13

resultado = busca_binaria_recursiva(lista, elemento, 0, len(lista) - 1)

if resultado != -1:
    print(f"Elemento {elemento} encontrado no índice {resultado}.")
else:
    print(f"Elemento {elemento} não encontrado na lista.")
