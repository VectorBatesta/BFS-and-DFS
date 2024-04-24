

#bfs ou dfs
escolhaProcura = 'dfs'




class nodeState:
    def __init__(self, matriz):
        self.matriz = matriz
        self.filhos = []



def procuraBFS(raiz: nodeState, nodeProcurar: nodeState):
    fila = [] #fila de nodes

    fila.append(raiz)

    #percorre até acabar
    while fila != []:
        nodeAtual = fila.pop(0)

        if nodeAtual == nodeProcurar:
            return 'achou'
        
        fila.append(nodeAtual.filhos)

    return 0 #nao achou



def procuraDFS(raiz: nodeState, nodeProcurar: nodeState):
    
    return 'achou'
    return 0 #nao achou



def gerar_filhos(nodePai: nodeState, raiz: nodeState):
    adicionarFilhos = [] #checa depois se há repetido

    #acha a posicao do zero pra fazer trocas
    for i in range(9):
        if nodePai.matriz[i] == 0:
            posicao = i
            break
        else:
            exit("caceta cade o zero")

    #[XX ]
    #[XX ]
    #[XX ]
    #troca direita
    if posicao in (0, 1, 3, 4, 6, 7):
        novoFilho = nodePai
        novoFilho.matriz[posicao] = novoFilho.matriz[posicao + 1]
        novoFilho.matriz[posicao + 1] = 0
        adicionarFilhos.append(novoFilho)

    #[ XX]
    #[ XX]
    #[ XX]
    #troca esquerda
    if posicao in (1, 2, 4, 5, 7, 8):
        novoFilho = nodePai
        novoFilho.matriz[posicao] = novoFilho.matriz[posicao - 1]
        novoFilho.matriz[posicao - 1] = 0
        adicionarFilhos.append(novoFilho)

    #[XXX]
    #[XXX]
    #[   ]
    #troca baixo
    if posicao in (0, 1, 2, 3, 4, 5):
        novoFilho = nodePai
        novoFilho.matriz[posicao] = novoFilho.matriz[posicao + 3]
        novoFilho.matriz[posicao + 3] = 0
        adicionarFilhos.append(novoFilho)

    #[   ]
    #[XXX]
    #[XXX]
    #troca cima
    if posicao in (3, 4, 5, 6, 7, 8):
        novoFilho = nodePai
        novoFilho.matriz[posicao] = novoFilho.matriz[posicao - 3]
        novoFilho.matriz[posicao - 3] = 0
        adicionarFilhos.append(novoFilho)


    while adicionarFilhos != []:
        proxFilho = adicionarFilhos.pop()
        match escolhaProcura:
            case 'bfs':
                achou = procuraBFS(raiz, proxFilho)
            case 'dfs':
                achou = procuraDFS(raiz, proxFilho)
        
        if achou == 0:
            nodePai.filhos.append(proxFilho)
        









        


def algoritmoDFS(raiz):
    pilha = []

    while procuraDFS(raiz) == 0:
        return
        




def algoritmoBFS(raiz):
    fila = []

    while procuraBFS(raiz) == 0:
        return
    

if __name__ == "__main__":
    #0 = vazio
    raiz = nodeState([1, 2, 4, 3, 0, 5, 6, 7, 8])
    objetivo =       [1, 2, 3, 4, 5, 6, 7, 8, 0]

    match escolhaProcura:
        case 'bfs':
            algoritmoBFS(raiz)
        case 'dfs':
            algoritmoDFS(raiz)
    

