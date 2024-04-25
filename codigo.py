import copy

#bfs ou dfs
escolhaProcura = 'dfs'




class nodeState:
    def __init__(self, matriz, pai = None, movimento = None, nivel = 0):
        self.matriz = matriz
        #self.filhos = []
        self.pai = pai
        self.movimento = movimento
        self.nivel = nivel
        # ...


"""
def procuraBFS(raiz: nodeState, nodeProcurar: nodeState):
    fila = [] #fila de nodes

    fila.append(raiz)

    #percorre até acabar
    while fila != []:
        nodeAtual = copy.deepcopy(fila.pop(0))

        if nodeAtual == nodeProcurar:
            return 'achou'
        
        if nodeAtual.filhos != []:
            fila.append(nodeAtual.filhos)

    return 0 #nao achou

def procuraDFS(raiz: nodeState, nodeProcurar: nodeState):
    pilha = [] #pilha de nodes
    
    pilha.append(raiz)
    
    #percorre até acabar
    while pilha != []:
        print(f'pilha: {pilha}\n')
        nodeAtual = copy.deepcopy(pilha.pop())
        print(f'nodeAtual: {nodeAtual}\n')

        if nodeAtual == nodeProcurar:
            return 'achou'
        
        print(nodeAtual.filhos)
        if nodeAtual.filhos != []:
            pilha.append(nodeAtual.filhos)

    return 0 #nao achou
"""


def gerar_filhos(nodePai: nodeState):
    listaGerada = []
    
    posicao = -1
    #acha a posicao do zero pra fazer trocas
    for i in range(9):
        if nodePai.matriz[i] == 0:
            posicao = i
            break
    if posicao == -1:
        exit(f'caceta cade o zero: {nodePai.matriz}')

    #[XX ]
    #[XX ]
    #[XX ]
    #troca direita
    if posicao in (0, 1, 3, 4, 6, 7):
        novoFilho = copy.deepcopy(nodePai) #cria copia ao inves de fazer referencia
        novoFilho.matriz[posicao] = novoFilho.matriz[posicao + 1]
        novoFilho.matriz[posicao + 1] = 0
        novoFilho.movimento = 'direita'
        novoFilho.nivel += 1
        novoFilho.pai = nodePai #apenas referencia do pai
        nodePai.filhos.append(novoFilho)
        
        listaGerada.append(novoFilho)
        # print(novoFilho.matriz)

    #[ XX]
    #[ XX]
    #[ XX]
    #troca esquerda
    if posicao in (1, 2, 4, 5, 7, 8):
        novoFilho = copy.deepcopy(nodePai) #cria copia ao inves de fazer referencia
        novoFilho.matriz[posicao] = novoFilho.matriz[posicao - 1]
        novoFilho.matriz[posicao - 1] = 0
        novoFilho.movimento = 'esquerda'
        novoFilho.nivel += 1
        novoFilho.pai = nodePai #apenas referencia do pai
        nodePai.filhos.append(novoFilho)
        
        listaGerada.append(novoFilho)
        # print(novoFilho.matriz)

    #[XXX]
    #[XXX]
    #[   ]
    #troca baixo
    if posicao in (0, 1, 2, 3, 4, 5):
        novoFilho = copy.deepcopy(nodePai) #cria copia ao inves de fazer referencia
        novoFilho.matriz[posicao] = novoFilho.matriz[posicao + 3]
        novoFilho.matriz[posicao + 3] = 0
        novoFilho.movimento = 'baixo'
        novoFilho.nivel += 1
        novoFilho.pai = nodePai #apenas referencia do pai
        nodePai.filhos.append(novoFilho)
        
        listaGerada.append(novoFilho)
        # print(novoFilho.matriz)

    #[   ]
    #[XXX]
    #[XXX]
    #troca cima
    if posicao in (3, 4, 5, 6, 7, 8):
        novoFilho = copy.deepcopy(nodePai) #cria copia ao inves de fazer referencia
        novoFilho.matriz[posicao] = novoFilho.matriz[posicao - 3]
        novoFilho.matriz[posicao - 3] = 0
        novoFilho.movimento = 'cima'
        novoFilho.nivel += 1
        novoFilho.pai = nodePai #apenas referencia do pai
        nodePai.filhos.append(novoFilho)
        
        listaGerada.append(novoFilho)
        # print(novoFilho.matriz)
        
    return listaGerada


        






































def BFS(raiz: nodeState, objetivo):
    ABERTOS = [raiz] #é uma pilha
    FECHADOS = []

    while ABERTOS != []:
        X = ABERTOS.pop() #() = ultimo
        
        if X.matriz == objetivo:
            return 'SUCESSO'
        else:
            ListaFilhos = gerar_filhos(X)
            FECHADOS.append(X)
            
            for node in ListaFilhos:
                if node in ABERTOS or node in FECHADOS:
                    ListaFilhos.remove(node) #evita ciclos ou loops
                    
            ABERTOS.append(ListaFilhos) #empilhar os estados na pilha
    return 'FALHA' #não restam mais estados


def DFS(raiz: nodeState, objetivo):
    ABERTOS = [raiz] #é uma fila
    FECHADOS = []
    
    while ABERTOS != []:
        X = ABERTOS.pop(0) #0 = primeiro
        
        if X.matriz == objetivo:
            return 'SUCESSO'
        else:
            ListaFilhos = gerar_filhos(X)
            FECHADOS.append(X)
            
            for node in ListaFilhos:
                if node in ABERTOS or node in FECHADOS:
                    ListaFilhos.remove(node) #evita ciclos ou loops
            
            ABERTOS.append(ListaFilhos) #enfileirar os estados na Fila
    return 'FALHA' #não restam mais estados
























        

"""
def algoritmoDFS(raiz: nodeState, objetivo = nodeState):
    pilha = []
    nodeAtual = copy.deepcopy(raiz)

    while procuraDFS(nodeAtual, objetivo) == 0:
        gerar_filhos(nodeAtual, raiz)
        pilha.append(nodeAtual.filhos)
        nodeAtual = pilha.pop() #() = ultimo valor colocado, portanto pilha
        
    print(f'\nachei! node: {nodeAtual.matriz}')



def algoritmoBFS(raiz: nodeState, objetivo = nodeState):
    fila = []
    nodeAtual = copy.deepcopy(raiz)

    while procuraBFS(nodeAtual, objetivo) == 0:
        gerar_filhos(nodeAtual, raiz)
        fila.append(nodeAtual.filhos)
        nodeAtual = fila.pop(0) #(0) = primeiro valor colocado, portanto fila
        
    print(f'\nachei! node: {nodeAtual.matriz}')
""" 
    
    
    

if __name__ == "__main__":
    #0 = vazio
    raiz = nodeState([1, 2, 4, 3, 0, 5, 6, 7, 8])
    matrizObjetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    match escolhaProcura:
        case 'bfs':
            BFS(raiz, matrizObjetivo)
        case 'dfs':
            DFS(raiz, matrizObjetivo)