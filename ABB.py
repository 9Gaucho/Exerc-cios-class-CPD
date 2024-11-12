class Produto:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def __repr__(self):
        return f"Produto(ID={self.id}, Nome={self.nome}, Preço={self.preco})"


class NoBST:
    def __init__(self, produto):
        self.produto = produto
        self.esquerda = None
        self.direita = None


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, produto):
        novo_no = NoBST(produto)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._inserir_recursivo(self.raiz, novo_no)

    def _inserir_recursivo(self, atual, novo_no):
        if novo_no.produto.id < atual.produto.id:
            if atual.esquerda is None:
                atual.esquerda = novo_no
            else:
                self._inserir_recursivo(atual.esquerda, novo_no)
        else:
            if atual.direita is None:
                atual.direita = novo_no
            else:
                self._inserir_recursivo(atual.direita, novo_no)

    def buscar(self, id):
        return self._buscar_recursivo(self.raiz, id)

    def _buscar_recursivo(self, atual, id):
        if atual is None:
            return None
        if id == atual.produto.id:
            return atual.produto
        elif id < atual.produto.id:
            return self._buscar_recursivo(atual.esquerda, id)
        else:
            return self._buscar_recursivo(atual.direita, id)

    def remover(self, id):
        self.raiz = self._remover_recursivo(self.raiz, id)

    def _remover_recursivo(self, atual, id):
        if atual is None:
            return atual

        if id < atual.produto.id:
            atual.esquerda = self._remover_recursivo(atual.esquerda, id)
        elif id > atual.produto.id:
            atual.direita = self._remover_recursivo(atual.direita, id)
        else:
            if atual.esquerda is None:
                return atual.direita
            elif atual.direita is None:
                return atual.esquerda

            temp = self._minimo_no(atual.direita)
            atual.produto = temp.produto
            atual.direita = self._remover_recursivo(atual.direita, temp.produto.id)
        return atual

    def _minimo_no(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def listar_ordenado(self):
        produtos = []
        self._inorder(self.raiz, produtos)
        return produtos

    def _inorder(self, atual, produtos):
        if atual:
            self._inorder(atual.esquerda, produtos)
            produtos.append(atual.produto)
            self._inorder(atual.direita, produtos)


produto1 = Produto(30, "Teclado", "Teclado mecânico", 150.0)
produto2 = Produto(20, "Mouse", "Mouse óptico", 50.0)
produto3 = Produto(40, "Monitor", "Monitor LED", 700.0)

arvore = ArvoreBinariaBusca()

arvore.inserir(produto1)
arvore.inserir(produto2)
arvore.inserir(produto3)

produto_buscado = arvore.buscar(20)
print(f"Produto encontrado: {produto_buscado}")

arvore.remover(30)

produtos_ordenados = arvore.listar_ordenado()
print("Produtos em ordem crescente de ID:", produtos_ordenados)
