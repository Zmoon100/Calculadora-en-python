class arbolbinario:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None
        self.contador = 1
        self.altura = 1

    def altura_nodo(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def actualizar_altura(self, nodo):
        if nodo:
            nodo.altura = 1 + max(self.altura_nodo(nodo.izquierda),
                                  self.altura_nodo(nodo.derecha))

    def factor_balance(self, nodo):
        if nodo is None:
            return 0
        return self.altura_nodo(nodo.izquierda) - self.altura_nodo(nodo.derecha)

  
    def rotacion_ll(self, nodo):
        print(f"Aplicando rotación LL en nodo {nodo.dato}")
        nueva_raiz = nodo.izquierda
        nodo.izquierda = nueva_raiz.derecha
        nueva_raiz.derecha = nodo
        self.actualizar_altura(nodo)
        self.actualizar_altura(nueva_raiz)
        return nueva_raiz

    def rotacion_rr(self, nodo):
        print(f"Aplicando rotación RR en nodo {nodo.dato}")
        nueva_raiz = nodo.derecha
        nodo.derecha = nueva_raiz.izquierda
        nueva_raiz.izquierda = nodo
        self.actualizar_altura(nodo)
        self.actualizar_altura(nueva_raiz)
        return nueva_raiz

    def rotacion_lr(self, nodo):
        print(f"Aplicando rotación LR en nodo {nodo.dato}")
        nodo.izquierda = self.rotacion_rr(nodo.izquierda)
        return self.rotacion_ll(nodo)

    def rotacion_rl(self, nodo):
        print(f"Aplicando rotación RL en nodo {nodo.dato}")
        nodo.derecha = self.rotacion_ll(nodo.derecha)
        return self.rotacion_rr(nodo)


    def insert(self, nodo, dato):
        if nodo is None:
            return arbolbinario(dato)
        if dato < nodo.dato:
            nodo.izquierda = self.insert(nodo.izquierda, dato)
        elif dato > nodo.dato:
            nodo.derecha = self.insert(nodo.derecha, dato)
        else:
            nodo.contador += 1
            return nodo

        self.actualizar_altura(nodo)
        balance = self.factor_balance(nodo)

        if balance > 1 and dato < nodo.izquierda.dato:
            return self.rotacion_ll(nodo)
        if balance < -1 and dato > nodo.derecha.dato:
            return self.rotacion_rr(nodo)
        if balance > 1 and dato > nodo.izquierda.dato:
            return self.rotacion_lr(nodo)
        if balance < -1 and dato < nodo.derecha.dato:
            return self.rotacion_rl(nodo)

        return nodo
    
    def preorden(self, nodo_actual):
        if nodo_actual:
            for _ in range(nodo_actual.contador):
                print(nodo_actual.dato, end=' ')
            self.preorden(nodo_actual.izquierda)
            self.preorden(nodo_actual.derecha)

    def inorden(self, nodo_actual):
        if nodo_actual:
            self.inorden(nodo_actual.izquierda)
            for _ in range(nodo_actual.contador):
                print(nodo_actual.dato, end=' ')
            self.inorden(nodo_actual.derecha)

    def postorden(self, nodo_actual):
        if nodo_actual:
            self.postorden(nodo_actual.izquierda)
            self.postorden(nodo_actual.derecha)
            for _ in range(nodo_actual.contador):
                print(nodo_actual.dato, end=' ')

def print_tree_sideways(node, level=0):
    if not node:
        return
    print_tree_sideways(node.derecha, level + 1)
    print("    " * level + f"{node.dato} (bal:{node.factor_balance(node)})")
    print_tree_sideways(node.izquierda, level + 1)


root = arbolbinario(7)
root = root.insert(root, 5)
root = root.insert(root, 9)
root = root.insert(root, 3)
root = root.insert(root, 6)
root = root.insert(root, 8)
root = root.insert(root, 10)

print("Recorrido en preorden:")
root.preorden(root)
print("\nRecorrido en inorden:")
root.inorden(root)
print("\nRecorrido en postorden:")
root.postorden(root)

print("\nÁrbol visualizado lateralmente:")
print_tree_sideways(root)

root = root.insert(root, 10)
root = root.insert(root, 10)

print("\n-Después de insertar 10 dos veces más-")
print("\nRecorrido en inorden:")
root.inorden(root)

print("\nÁrbol visualizado lateralmente después de insertar:")
print_tree_sideways(root)
