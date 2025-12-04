class arbolbinario:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None
        self.contador = 1   

    def insert(self, nodo, dato):
        if nodo is None:
            return arbolbinario(dato)
        else:
            if dato < nodo.dato:
                nodo.izquierda = self.insert(nodo.izquierda, dato)
            elif dato > nodo.dato:
                nodo.derecha = self.insert(nodo.derecha, dato)
            else:
                nodo.contador += 1
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

    def encontrar_maximo(self, nodo):
        actual = nodo
        while actual.derecha is not None:
            actual = actual.derecha
        return actual

    def delete(self, nodo, dato):
        if nodo is None:
            return nodo
        if dato < nodo.dato:
            nodo.izquierda = self.delete(nodo.izquierda, dato)
        elif dato > nodo.dato:
            nodo.derecha = self.delete(nodo.derecha, dato)
        else:
            if nodo.contador > 1:
                nodo.contador -= 1
                return nodo
            if nodo.izquierda is None and nodo.derecha is None:
                return None
            elif nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            else:
                max_izq = self.encontrar_maximo(nodo.izquierda)
                nodo.dato = max_izq.dato
                nodo.contador = max_izq.contador
                max_izq.contador = 1  
                nodo.izquierda = self.delete(nodo.izquierda, max_izq.dato)
                return nodo 


root = arbolbinario(7)
root.insert(root, 5)
root.insert(root, 9)
root.insert(root, 3)
root.insert(root, 6)
root.insert(root, 8)
root.insert(root, 10)

print("Recorrido en preorden:")
root.preorden(root)
print("\nRecorrido en inorden:")
root.inorden(root)
print("\nRecorrido en postorden:")
root.postorden(root)

root.insert(root, 10)  
root.insert(root, 10)  
print("\n-Después de insertar 10 dos veces más-")
print("\nRecorrido en inorden:")
root.inorden(root)

print("\nEliminando nodo 10 (con contador)...")
root = root.delete(root, 10)

print("\nRecorrido en inorden después de delete:")
root.inorden(root)
