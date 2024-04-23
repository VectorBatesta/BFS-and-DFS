

#bfs ou dfs
escolhaProcura = 'bfs'




class nodeState:
    def __init__(self, matriz):
        self.matriz = matriz
        self.filhos = []

def procuraBFS(raiz):
    FAZER]
    return 'achou'
    return #nao achou

def procuraDFS(raiz):
    FAZER]
    return 'achou'
    return #nao achou



def gerar_filhos(node: nodeState):
    adicionarFilhos = [] #checa depois se há repetido

    #acha a posicao do zero pra fazer trocas
    for i in range(9):
        if node.matriz[i] == 0:
            posicao = i
            break
        else:
            exit("caceta cade o zero")

    #[XX ]
    #[XX ]
    #[XX ]
    #troca direita
    if posicao in (0, 1, 3, 4, 6, 7):
        novoFilho = nodeState(node.matriz)
        novoFilho.matriz[posicao] = novoFilho.matriz[posicao + 1]
        novoFilho.matriz[posicao + 1] = 0
        adicionarFilhos.append(novoFilho)

    #[ XX]
    #[ XX]
    #[ XX]
    #troca esquerda
    if posicao in (1, 2, 4, 5, 7, 8):
        novoFilho = nodeState(node.matriz)
        novoFilho.matriz[posicao] = novoFilho.matriz[posicao - 1]
        novoFilho.matriz[posicao - 1] = 0
        adicionarFilhos.append(novoFilho)

    #[XXX]
    #[XXX]
    #[   ]
    #troca baixo
    if posicao in (0, 1, 2, 3, 4, 5):
        novoFilho = nodeState(node.matriz)
        novoFilho.matriz[posicao] = novoFilho.matriz[posicao + 3]
        novoFilho.matriz[posicao + 3] = 0
        adicionarFilhos.append(novoFilho)

    #[   ]
    #[XXX]
    #[XXX]
    #troca cima
    if posicao in (3, 4, 5, 6, 7, 8):
        novoFilho = nodeState(node.matriz)
        novoFilho.matriz[posicao] = novoFilho.matriz[posicao - 3]
        novoFilho.matriz[posicao - 3] = 0
        adicionarFilhos.append(novoFilho)


    while adicionarFilhos != []:
        proxFilho = adicionarFilhos.pop()
        match escolhaProcura:
            case 'bfs'
        









        


def algoritmoDFS(raiz):
    pilha = []

    while procuraDFS(raiz) != 'achou':
        




def algoritmoBFS(raiz):
    

if __name__ == "__main__":
    #0 = vazio
    raiz = nodeState([1, 2, 4, 3, 0, 5, 6, 7, 8])
    objetivo =       [1, 2, 3, 4, 5, 6, 7, 8, 0]
    
    match escolhaProcura:
        case 'bfs':
            algoritmoBFS(raiz)
        case 'dfs':
            algoritmoDFS(raiz)
    

