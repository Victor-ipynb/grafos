class Grafo:
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.v = len(vertices)
        self.matriz = False
        self.lista = False
        self.valores = list(vertices.values())
    
    def iniciar_matriz(self):
        self.matriz = [[0]*self.v for i in range(self.v)]
        self.peso = [[[]]*self.v for i in range(self.v)]
    
    def iniciar_lista(self):
        self.lista = [[]*self.v for i in range(self.v)]
    
    def adicionar_aresta(self, inicio, fim, orient, peso): #orient: 0 para uma aresta orientada, 1 para não-orientada.
        if self.matriz:
            self.matriz[inicio-1][fim-1] += 1
            self.peso[inicio-1][fim-1] = self.peso[inicio-1][fim-1] + [peso]
            if inicio != fim and orient:
                self.matriz[fim-1][inicio-1] += 1
                self.peso[fim-1][inicio-1] = self.peso[fim-1][inicio-1] + [peso]
        
        if self.lista:
            self.lista[inicio-1].append([fim, peso])
            if inicio != fim and orient:
                self.lista[fim-1].append([inicio, peso])
    
    def mostrar_grafo(self):
        if self.matriz:
            for i in self.matriz:
                print(i)
                
            print('\n')
            
            for i in self.peso:
                print(i)
            
            print('\n')
        
        if self.lista:
            for i in range(self.v):
                print(f'{i+1}:', end='')
                for j in self.lista[i]:
                    print(f' -> {j}', end='')
                print('\n')
