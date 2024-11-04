# Lista ordenada
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Elemento que queremos buscar
elemento = 9

# Chamando a função de pesquisa Fibonacci
resultado = pesquisa_fibonacci(lista, elemento)

if resultado != -1:
    print(f"Elemento {elemento} encontrado no índice {resultado}.")
else:
    print(f"Elemento {elemento} não encontrado na lista.")
