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
        self.tiles = tiles.copy()
        self.solution = self.sort(tiles)
        self.board = list(self.split(tiles))
        

    def is_goal(self):
        # TODO: este método verifica se o tabuleiro atual é uma solução
        # do problema. O metódo deve retornar True se o tabuleiro for uma
        # solução e False se não for.
        if self.tiles == self.solution:
            return True
        return False

    def heuristic(self):
        # TODO: este método calcula a função heurística para o estado
        # representado pelo tabuleiro. A heurística usada deve retornar o
        # valor da contagem de quantos números estão na posição errada em
        # relação ao objetivo. Por exemplo, o estado
        # [2, 1, 3, 4, 5, 6, 7, 8, "x"] tem valor 2 para heurística, pois
        # o número "1" está na posição errada e o número "2" também.
        # Este método deve retornar o valor da função heurística.
        count = 0
        for i in range(len(self.solution)):
            if self.tiles[i] != self.solution[i]:
                count+=1
        return count

    def split(self, tiles):
        # Dividir os tiles em uma matriz para melhor trabalhar as coordenadas.
        temp = tiles.copy()
        n = 1
        for i in range(len(temp)):
            if i*i == len(temp):
                n = i
        for i in range(0, len(temp), n):
            yield temp[i:i + n]
        return temp

    def sort(self,tiles):
        # Ordena o tiles para gerar a solução do puzzle de forma dinâmica
        temp = tiles.copy()
        temp[temp.index('x')] = 0
        temp[temp.index(0)] = max(temp)+1
        temp.sort()
        temp[temp.index(max(temp))] = 'x'
        return temp

    def coordinates(self,i,y):
        # Retorna as cordenadas possíveis dos vizinhos de x de forma dinâmica
        coord = []
        for i in range(4):
            if i < 1:
                coord.append((i,y-1))
                coord.append((i,y+1))
            else:
                coord.append((i-1,y))
                coord.append((i+1,y))
        return coord
    
    def change_positions(self,neighbor):
        # Muda a posição do elemento.
        temp_tiles = self.tiles.copy()
        pos_neighbor = temp_tiles.index(neighbor)
        pos_x = temp_tiles.index('x')
        temp_tiles[pos_x]=neighbor
        temp_tiles[pos_neighbor]='x'
        b = Board(temp_tiles)
        return b

    def find_x(self):
        # Encontra a posição de x na matriz.
        for i in range(len(self.board)):
            for y in range(len(self.board[i])):
                if self.board[i][y] == 'x':
                    return (i,y)

    def get_neighbors(self):
        # TODO: Este método deve retornar uma lista com os vizinhos do estado
        # representado pelo tabuleiro. Os vizinhos são os possíveis novos
        # tabuleiros resultantes da movimentação das peças do tabuleiro atual.
        # A lista retornada é uma lista de objetos da classe Board.
        objects = []
        x = self.find_x()
        proced = self.coordinates(x[0],x[1])
        for x,y in proced:
            if x != -1 and y != -1:
                try:
                    neighbor = self.board[x][y]
                    objects.append(self.change_positions(neighbor))
                except IndexError:
                    pass
        return objects

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
        #Printa o board de forma dinâmica aceitando qualquer proporção de matriz.
        temp = list(self.split(self.tiles.copy()))
        for i in temp:
            print(i)


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
        cost = [node.cost for node in self.frontier]
        return self.frontier.pop(cost.index(min(cost)))

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
        neighbors = self.current_node.state.get_neighbors()
        for neighbor in neighbors:
            node = Node(neighbor, neighbor.heuristic())
            if self.is_neighbor_in_frontier(node.state):
                if node.state not in self.explored:
                    node.parent = self.current_node
                    self.frontier.append(node)

    def is_neighbor_in_frontier(self, neighbor):
        """
        Este método avalia se algum nó da fronteira contém o estado (neighbor).
        Você pode utilizar este método para implementar o update_frontier.
        """
        for node in self.frontier:
            if node.state == neighbor:
                return False
        return True

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
        path = [node.state]
        for i in self.initial_state.tiles:
            path.append(node.parent.state)
            node = node.parent
        path.reverse()
        return path

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
    tiles = [3, 2, 8, 1, 5, 4, 'x', 7 , 6]
    initial_state = Board(tiles)
    astar = AStar(initial_state)
    final_node = astar.search()
    path = astar.get_path(final_node)
    for state in path:
        state.print_board()
        print("---")
