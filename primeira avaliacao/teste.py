# # tiles = [2, 1, 3, 5,'x',4, 6, 7, 8]

# # def sort(tiles):
# #     temp = tiles.copy()
# #     temp[temp.index('x')] = 0
# #     temp[temp.index(0)] = max(temp)+1
# #     temp.sort()
# #     temp[temp.index(max(temp))] = 'x'
# #     return temp

# # print(sort(tiles))
# def chunks(lista, n):
#     for i in range(0, len(lista), n):
#         yield lista[i:i + n]

# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# print(list(chunks(l, 3)))




        
# # board = [
# #     tiles[:3],
# #     tiles[3:6],
# #     tiles[6:]
# # ]
# # print(board)

# # def achax(board):
# #     #Pesquisa no 'board' em qual coluna e indice o valor 'x' se encontra;
# #     # sendo o valor 'x' o valor vazio do tabuleiro;
# #     for i in range(len(board)):
# #         for y in range(len(board[i])):
# #             if board[i][y] == 'x':
# #                 return(i,y)


# # def procedimentos(i,y):
# #     # Essa função tem como objetivo pegar todos os possiveis lados
# #     # de um indice y
# #     # de uma coluna i;
# #     return[[i,y-1],[i,y+1],[i-1,y],[i+1,y]]

# # def change_pos(tiles,neighbor):
# #     temp = tiles.copy()
# #     id = temp.index(neighbor)
# #     x = temp.index('x')
# #     temp[x]=neighbor
# #     temp[id]='x'
# #     return temp

# # def chunks(lista):
# #     n = 0
# #     for i in range(len(lista)):
# #         if i*i == len(lista)+1:
# #             n = i
# #     for i in range(0, len(lista), n):
# #         yield lista[i:i + n]

# # print(list(chunks(tiles)))

# # def mostracasas(board):
# #     objects = []
# #     x = achax(board)
# #     proced = procedimentos(x[0],x[1])
# #     for i in proced:
# #         try:
# #             print("suahsuas",board[i[0]][i[1]])
# #             objects.append(change_pos(tiles,board[i[0]][i[1]]))
            
# #         except KeyError:
# #             pass
# #     print(objects)
# #     return objects 

# #mostracasas(board)

# # frontier = [1,5,8,9,100]
# # cost = [r for r in frontier]
# # for node in frontier:
# #     cost.append(node)
# # print(frontier.pop(cost.index(min(cost))))
# # print(frontier)
