tiles = [2, 1, 3, 5,'x',4, 6, 7, 8]
board = {1:tiles[:3],
        2:tiles[3:6],
        3:tiles[6:]}


def achax(board):
    #Pesquisa no 'board' em qual coluna e indice o valor 'x' se encontra;
    # sendo o valor 'x' o valor vazio do tabuleiro;
    for i in board:
        for y in range(len(board[i])):
            if board[i][y] == 'x':
                return[i,y]


def procedimentos(i,y):
    # Essa função tem como objetivo pegar todos os possiveis lados
    # de um indice y
    # de uma coluna i;
    return[[i,y-1],[i,y+1],[i-1,y],[i+1,y]]

def change_pos(board,neighbor):
    temp = board.copy()
    id = temp.index(neighbor)
    x = temp.index('x')
    temp[x]=neighbor
    temp[id]='x'
    return temp

def mostracasas(board):
    objects = []
    x = achax(board)
    proced = procedimentos(x[0],x[1])
    for i in proced:
        try:
            print("suahsuas",board[i[0]][i[1]])
            objects.append(change_pos(tiles,board[i[0]][i[1]]))
            
        except:
            pass
    print(objects)
    return objects 

frontier = [1,5,8,9,100]
cost = []
for node in frontier:
    cost.append(node)
print(frontier.pop(cost.index(max(cost))))
print(frontier)