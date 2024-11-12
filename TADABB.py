class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ABB:
    def __init__(self):
        self.root = None

    def inserir(self, value):
        self.root = self._inserir_recursivo(self.root, value)

    def _inserir_recursivo(self, node, value):
        if node is None:
            return Node(value)
        elif value < node.value:
            node.left = self._inserir_recursivo(node.left, value)
        else:
            node.right = self._inserir_recursivo(node.right, value)
        return node

    def buscar(self, value):
        return self._buscar_recursivo(self.root, value)

    def _buscar_recursivo(self, node, value):
        if node is None or node.value == value:
            return node
        elif value < node.value:
            return self._buscar_recursivo(node.left, value)
        else:
            return self._buscar_recursivo(node.right, value)

    def deletar(self, value):
        self.root = self._deletar_recursivo(self.root, value)

    def _deletar_recursivo(self, node, value):
        if node is None:
            return node
        if value < node.value:
            node.left = self._deletar_recursivo(node.left, value)
        elif value > node.value:
            node.right = self._deletar_recursivo(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._get_min(node.right)
            node.value = min_larger_node.value
            node.right = self._deletar_recursivo(node.right, min_larger_node.value)
        return node

    def _get_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def imprimir_pre_ordem(self):
        self._imprimir_pre_ordem_recursivo(self.root)

    def _imprimir_pre_ordem_recursivo(self, node):
        if node:
            print(node.value, end=' ')
            self._imprimir_pre_ordem_recursivo(node.left)
            self._imprimir_pre_ordem_recursivo(node.right)

    def imprimir_pos_ordem(self):
        self._imprimir_pos_ordem_recursivo(self.root)

    def _imprimir_pos_ordem_recursivo(self, node):
        if node:
            self._imprimir_pos_ordem_recursivo(node.left)
            self._imprimir_pos_ordem_recursivo(node.right)
            print(node.value, end=' ')

    def imprimir_ordem_simetrica(self):
        self._imprimir_ordem_simetrica_recursivo(self.root)

    def _imprimir_ordem_simetrica_recursivo(self, node):
        if node:
            self._imprimir_ordem_simetrica_recursivo(node.left)
            print(node.value, end=' ')
            self._imprimir_ordem_simetrica_recursivo(node.right)

# Exemplo de uso
abb = ABB()
abb.inserir(50)
abb.inserir(30)
abb.inserir(70)
abb.inserir(20)
abb.inserir(40)
abb.inserir(60)
abb.inserir(80)

print("Pré-ordem:")
abb.imprimir_pre_ordem()  
print("\nOrdem simétrica:")
abb.imprimir_ordem_simetrica()  

print("\nPós-ordem:")
abb.imprimir_pos_ordem()  


print("\nBuscar 40:", abb.buscar(40))  

abb.deletar(70)
print("\nOrdem simétrica após deletar 70:")
abb.imprimir_ordem_simetrica()  
