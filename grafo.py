class Grafo:
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.v = len(vertices)
        self.matriz = False
        self.lista = False
        self.valores = list(vertices.values())
        self.nomes = list(vertices.keys())
        self.rotas = [[None]*self.v for i in range(self.v)]
        self.brotas = [[False]*self.v for i in range(self.v)]
        self.caminhos = []
        self.mapa = [[None]*self.v for i in range(self.v)]
    
    def iniciar_matriz(self):
        self.matriz = [[0]*self.v for i in range(self.v)]
        self.peso = [[[]]*self.v for i in range(self.v)]
    
    def iniciar_lista(self):
        self.lista = [[]*self.v for i in range(self.v)]
    
    def adicionar_aresta(self, inicio, fim, orient, peso): #orient: 0 para uma aresta orientada, 1 para não-orientada.
        if self.matriz:
            self.matriz[inicio][fim] += 1
            self.peso[inicio][fim] = self.peso[inicio][fim] + [peso]
            if inicio != fim and orient:
                self.matriz[fim][inicio] += 1
                self.peso[fim][inicio] = self.peso[fim][inicio] + [peso]
        
        if self.lista:
            self.lista[inicio].append([fim, peso])
            if inicio != fim and orient:
                self.lista[fim].append([inicio, peso])
    
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
                print(f'{i}:', end='')
                for j in self.lista[i]:
                    print(f' -> {j}', end='')
                print('\n')
    
    def calcular_rotas(self, inicio, fim, carga = 0, atual = None, percurso = ''):
        if atual == None:
            self.rotas[inicio][inicio] = 0
            self.brotas[inicio][inicio] = True
            atual = inicio
            percurso = self.nomes[atual]
            self.mapa[inicio][atual] = percurso
        for i in range(len(self.lista[atual])):
            if self.brotas[inicio][self.lista[atual][i][0]] == False:
                if self.rotas[inicio][self.lista[atual][i][0]]:
                    if self.rotas[inicio][self.lista[atual][i][0]] > carga + self.lista[atual][i][1]:
                        self.rotas[inicio][self.lista[atual][i][0]] = carga + self.lista[atual][i][1]
                        self.caminhos.append([carga + self.lista[atual][i][1], self.lista[atual][i][0], percurso + '-' + self.nomes[self.lista[atual][i][0]]])
                else:
                    self.rotas[inicio][self.lista[atual][i][0]] = carga + self.lista[atual][i][1]
                    self.caminhos.append([carga + self.lista[atual][i][1], self.lista[atual][i][0], percurso + '-' + self.nomes[self.lista[atual][i][0]]])
        self.caminhos.sort(key=lambda x: x[0])
        if self.caminhos:
            self.brotas[inicio][self.caminhos[0][1]] = True
            self.mapa[inicio][self.caminhos[0][1]] = self.caminhos[0][2]
            t = self.caminhos[0]
            delete = []
            contador = 0
            for i in self.caminhos:
                if i[1] == t[1]:
                    delete.append(contador)
                contador += 1
            for i in delete[::-1]:
                self.caminhos.pop(i)
            self.calcular_rotas(inicio, fim, *t)

class Barvore(Grafo):
    
    def __init__(self, vertices):
        super().__init__(vertices)
        self.arvore = []
    
    def BB_comparar(self, elemento, c = 0):
        while len(self.arvore) <= c:
            self.arvore.append(None)
            
        if self.arvore[c]:
            if elemento > self.arvore[c]:
                self.BB_comparar(elemento, 2*c+2)
            elif elemento < self.arvore[c]:
                self.BB_comparar(elemento, 2*c+1)
        else:
            self.arvore[c] = elemento
    
    def BB_buscar(self, elemento, c = 0):
        if self.arvore[c]:
            if elemento == self.arvore[c]:
                print(c)
                return c
            elif elemento > self.arvore[c]:
                self.BB_buscar(elemento, 2*c+2)
            else:
                self.BB_buscar(elemento, 2*c+1)
    
    def transformar_em_BB(self):
        for i in range(self.v):
            self.BB_comparar(self.valores[i])
    
    def heap_subir(self, c):
        if len(self.arvore) > 2*c+1:
            e = self.arvore[2*c+1]
        if len(self.arvore) > 2*c+2:
            d = self.arvore[2*c+2]
            if e > d:
                t = (e,1)
            else:
                t = (d,2)
        else:
            t = (e,1)
        if t[0] > self.arvore[c]:
            self.arvore[2*c+t[1]] = self.arvore[c]
            self.arvore[c] = t[0]
            if c == 0:
                return None
            elif int(c/2) == c/2:
                self.heap_subir(int(c/2)-1)
            else:
                self.heap_subir(int(c/2))
    
    def heap_descer(self, c = 0):
        if len(self.arvore) > 2*c+1:
            e = self.arvore[2*c+1]
        else:
            return None
        if len(self.arvore) > 2*c+2:
            d = self.arvore[2*c+2]
            if e > d:
                t = (e,1)
            else:
                t = (d,2)
        else:
            t = (e,1)
        if t[0] > self.arvore[c]:
            self.arvore[2*c+t[1]] = self.arvore[c]
            self.arvore[c] = t[0]
            self.heap_descer(2*c+t[1])
            
    def heap_adicionar(self, elemento):
        self.arvore.append(elemento)
        self.heap_subir(int(len(self.arvore)/2)-1)
    
    def heap_remover(self):
        self.arvore[0] = self.arvore[-1]
        self.arvore.pop()
        self.heap_descer()
    
    def transformar_em_heap(self):
        for i in range(self.v):
            self.heap_adicionar(self.valores[i])
        