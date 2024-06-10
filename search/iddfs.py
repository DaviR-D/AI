from dls import DepthLimitedSearch
from graph import graph

nome_origem = input("Digite a cidade de origem: ")
nome_destino = input("Digite a cidade de destino: ")

start_city = graph[nome_origem]
goal_city = graph[nome_destino]

success = None
limit = 1

while(not success):
    success = DepthLimitedSearch(start_city, goal_city, limit).search()
    limit += 1
