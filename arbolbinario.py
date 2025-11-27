#Arbol binario preorden y postorden e inorden
class arbolbinario:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None 

    def preorden(self, nodo_actual):
        if nodo_actual:
            print(nodo_actual.dato, end=' ')
            self.preorden(nodo_actual.izquierda)
            self.preorden(nodo_actual.derecha)

    def inorden(self, nodo_actual):
        if nodo_actual:
            self.inorden(nodo_actual.izquierda)
            print(nodo_actual.dato, end=' ')
            self.inorden(nodo_actual.derecha)

    def postorden(self, nodo_actual):
        if nodo_actual:
            self.postorden(nodo_actual.izquierda)
            self.postorden(nodo_actual.derecha)
            print(nodo_actual.dato, end=' ')

root = arbolbinario('R')
nodeA = arbolbinario('A')
nodeB = arbolbinario('B')
nodeC = arbolbinario('C')
nodeD = arbolbinario('D')
nodeE = arbolbinario('E')
nodeF = arbolbinario('F')
nodeG = arbolbinario('G')

root.izquierda = nodeA
root.derecha = nodeB

nodeA.izquierda = nodeC
nodeA.derecha = nodeD

nodeB.izquierda = nodeE
nodeB.derecha = nodeF

nodeF.izquierda = nodeG

print("Recorrido en preorden:")
root.preorden(root)
print("\nRecorrido en inorden:")
root.inorden(root)
print("\nRecorrido en postorden:")
root.postorden(root)
