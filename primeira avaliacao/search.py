################################################################################
#
# Este é o exercício da 1a avaliação da disciplina de IA.
#
# O código traz um esqueleto para a implementação da busca A* para
# resolver o problema do quebra-cabeça de 8 números.
#
# O Objetivo do exercício é implementar o que falta da busca no código abaixo.
# Os métodos que precisam ser implementados estão com a marcação "TODO" seguida
# de uma descrição do que precisa ser feito.
#
# Leia atentamente todo os comentários no código.
#
# Se o programa estiver executando corretamente, ele deve exibir todas as
# configurações do tabuleiro do quebra cabeça dos 8 números para sair do estado
# final até chegar ao objetivo.
#
################################################################################

import random


class Board(object):
    """
    Esta classe representa uma configuração do tabuleiro do
    quebra-cabeça. O tabuleiro é um estado no problema de busca.
    
    O tabuleiro tem 9 posições (em inglês tiles), sendo 8 posições dedicadas
    aos números de 1 até 8 e uma posição especial "x" que representa a posição
    vazia.
 
    O tabuleiro é representado de forma linear, por exemplo,
    [1, 2, 3, 4, 5, 6, 7, 8, "x"], que visualmente representa o tabuleiro:

                                   1  2  3
                                   4  5  6
                                   7  8  x
    """

    def __init__(self, tiles):
        """
        Construtor.

        tiles é uma lista com as posições do tabuleiro, por exemplo,
        [1, 2, 3, 4, 5, 6, 7, 8, "x"].
        """
        self.tiles = tiles

    def is_goal(self):
        # TODO: este método verifica se o tabuleiro atual é uma solução
        # do problema. O metódo deve retornar True se o tabuleiro for uma
        # solução e False se não for.
        pass

    def heuristic(self):
        # TODO: este método calcula a função heurística para o estado
        # representado pelo tabuleiro. A heurística usada deve retornar o
        # valor da contagem de quantos números estão na posição errada em
        # relação ao objetivo. Por exemplo, o estado
        # [2, 1, 3, 4, 5, 6, 7, 8, "x"] tem valor 2 para heurística, pois
        # o número "1" está na posição errada e o número "2" também.
        # Este método deve retornar o valor da função heurística.
        pass

    def get_neighbors(self):
        # TODO: Este método deve retornar uma lista com os vizinhos do estado
        # representado pelo tabuleiro. Os vizinhos são os possíveis novos
        # tabuleiros resultantes da movimentação das peças do tabuleiro atual.
        # A lista retornada é uma lista de objetos da classe Board.
        pass

    
    # Os métodos a seguir dessa classe não devem ser modificados
    def __eq__(self, other):
        return self.tiles == other.tiles

    def __hash__(self):
        return hash(tuple(self.tiles))

    def __str__(self):
        return str(self.tiles)

    def __repr__(self):
        return str(self.tiles)

    def print_board(self):
        print(self.tiles[:3])
        print(self.tiles[3:6])
        print(self.tiles[6:])


class Node(object):
    """
    Esta classe representa um nó na busca. Cada nó contém um estado (tabuleiro),
    um custo e o pai do nó, este último é a referência para um outro nó.

    Esta classe não deve ser modificada.
    """
    
    def __init__(self, state, cost):
        """
        Construtor.

        state é um objeto da classe Board.
        cost é um número que representa o custo do nó.
        """
        self.state = state
        self.cost = cost
        self.parent = None

    def __str__(self):
        return str(self.state.tiles) + " - " + str(self.cost)

    def __repr__(self):
        return str(self.state.tiles) + " - " + str(self.cost)


class AStar(object):
    """
    Esta classe é responsável por fazer a busca A*. Ela recebe um estado
    inicial no construtor indicando a configuração inicial do tabuleiro do
    quebra cabeça.
    """
    
    def __init__(self, initial_state):
        """
        Construtor.

        initial_state é o estado inicial, ou seja, a configuração inicial do
        tabuleiro.

        No construtor também é iniciada a fronteira e o conjunto dos
        explorados. Note que a fronteira é uma lista de objetos da classe Node.
        """
        self.initial_state = initial_state
        self.frontier = [Node(self.initial_state, 0 + self.initial_state.heuristic())]
        self.explored = set()
        self.current_node = None

    def choose_from_frontier(self):
        # TODO: Este método remove e retorna o nó com menor custo da
        # fronteira.
        pass

    def update_frontier(self):
        # TODO: Este método é executado após ser escolhido um estado da
        # fronteira. No método search (encontrado mais abaixo), o estado
        # selecionado é atribuido a variável self.current_node. Assim,
        # esse método deve atualizar a fronteira com os vizinhos do estado
        # contido em self.current_node.
        #
        # Ao adicionar um nó na fronteira, lembre-se do cálculo do seu custo,
        # de gravar a referência para o nó pai e das regras existentes para
        # adicionar ou não um novo nó.
        #
        # Este método não precisa retornar a fronteira, já que ela pode ser
        # acessada em toda classe através da variável self.frontier.
        pass

    def is_neighbor_in_frontier(self, neighbor):
        """
        Este método avalia se algum nó da fronteira contém o estado (neighbor).
        Você pode utilizar este método para implementar o update_frontier.
        """
        for node in self.frontier:
            if node.state == neighbor:
                return True
        
        return False

    def get_path(self, node):
        # TODO: Este método retorna o caminho feito do estado inicial até o
        # nó passado como parâmetro (node).
        #
        # O retorno deve ser uma lista, que começa com o estado inicial e
        # termina com o estado do nó passado como parâmetro (node).
        #
        # Por exemplo, se a partir de um nó A, para chegar a um nó D, o
        # o algoritmo passou pelos nós B e C, então o retorno deve ser a lista
        # [A, B, C, D].
        #
        # Passando o nó objetivo encontrado pela busca como parâmetro dessa
        # função, tem-se como resultado o caminho completo para sair do estado
        # inicial e chegar no objetivo.
        pass

    def search(self):
        """
        Este método executa a busca A* para resolver o problema do
        quebra-cabeça de 8 números.

        Atenção: Para algumas configurações de tabuleiro, a solução pode ser
        impossível, causando um loop infinito.
        """
        while True:
            if len(self.frontier) == 0:
                return False

            self.current_node = self.choose_from_frontier()

            self.explored.add(self.current_node.state)

            if self.current_node.state.is_goal():
                return self.current_node

            self.update_frontier()
            

if __name__ == "__main__":
    # Para testar o algoritmo, o quebra-cabeça pode ser iniciado
    # de forma aleatória ou com um tabuleiro fixo.
    #
    # Abaixo temos as duas opções. Comente ou descomente as linhas
    # correspondentes para usar a opção desejada.
    #
    # Para testes iniciais, aconselho usar o tabuleiro fixo, pois
    # essa é uma configuração que temos certeza que tem solução.


    # Iniciando o quebra-cabeça de forma aleatória
    # tiles = [1, 2, 3, 4, 5, 6, 7, 8, "x"]
    # random.shuffle(tiles)
    
    # Iniciando o quebra-cabeça com um tabuleiro fixo
    tiles = [3, 2, 8, 1, 5, 4, 7, 6, "x"]
    initial_state = Board(tiles)

    astar = AStar(initial_state)
    final_node = astar.search()
    path = astar.get_path(final_node)

    for state in path:
        state.print_board()
        print("---")
