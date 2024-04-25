import copy



class nodeState:
    def __init__(self, matriz, pai = None, movimento = None, nivel = 0):
        self.matriz = matriz
        self.filhos = []
        self.pai = pai
        self.movimento = movimento
        self.nivel = nivel
        # ...
        
        


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


        




def printanode(X: nodeState):
    for i in range(9):
        if X.matriz[i] == 0:
            X.matriz[i] = ' '
    
    print(f'matriz: ', end='')
    for i in range(3):
        print(f'{X.matriz[i]}, ', end='')
    print(f'   nivel: {X.nivel},   movimento: {X.movimento}\n        ', end='')
    for i in range(3, 6):
        print(f'{X.matriz[i]}, ', end='')
    print(f'\n        ', end='')
    for i in range(6, 9):
        print(f'{X.matriz[i]}, ', end='')
    print(f'\n')
          
    for i in range(9):
        if X.matriz[i] == ' ':
            X.matriz[i] = 0










def BFS(raiz: nodeState, objetivo):
    ABERTOS = [raiz] #é uma pilha
    FECHADOS = []

    while ABERTOS != []:
        X = ABERTOS.pop(0) #(0) = primeiro
        
        printanode(X)
        
        if X.matriz == objetivo:
            return 'SUCESSO'
        else:
            if X.nivel <= 10:
                ListaFilhos = gerar_filhos(X)
                FECHADOS.append(X)
                
                for node in ListaFilhos:
                    if node in ABERTOS or node in FECHADOS:
                        ListaFilhos.remove(node) #evita ciclos ou loops
                        
                for node in ListaFilhos:
                    ABERTOS.append(node) #enfileirar os estados na Fila
            else:
                break
    return 'FALHA' #não restam mais estados


def DFS(raiz: nodeState, objetivo):
    ABERTOS = [raiz] #é uma pilha
    FECHADOS = []
    
    while ABERTOS != []:
        X = ABERTOS.pop() #() = ultimo
        
        printanode(X)
        
        if X.matriz == objetivo:
            return 'SUCESSO'
        else:
            if X.nivel <= 10:
                ListaFilhos = gerar_filhos(X)
                FECHADOS.append(X)
                
                for node in ListaFilhos:
                    if node in ABERTOS or node in FECHADOS:
                        ListaFilhos.remove(node) #evita ciclos ou loops
                
                for node in ListaFilhos:
                    ABERTOS.append(node) #enfileirar os estados na Fila
            else:
                break
    return 'FALHA' #não restam mais estados






    

if __name__ == "__main__":
    #0 = vazio
    raiz = nodeState([1, 2, 3, 4, 5, 6, 7, 0, 8])
    matrizObjetivo = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    match 'bfs':
        case 'bfs':
            print(BFS(raiz, matrizObjetivo))
        case 'dfs':
            print(DFS(raiz, matrizObjetivo))