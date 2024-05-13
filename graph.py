from node import Node

def connectNodes(n1, n2, weight):
    n1.addConection(n2, weight)
    n2.addConection(n1, weight)

cities = ['Oradea',
           'Zerind',
           'Arad',
           'Timisoara',
           'Lugoj',
           'Mehadia',
           'Dobreta',
           'Sibiu',
           'Fagaras',
           'Rimnicu Vilcea',
           'Pitesti',
           'Craiova',
           'Bucharest',
           'Giurgiu',
           'Urziceni',
           'Neamt',
           'Iasi',
           'Vaslui',
           'Hirsova',
           'Eforie']

graph = dict()

for city in cities:
    graph[city] = Node(city)
    
connectNodes(graph['Oradea'], graph['Zerind'], 71)
connectNodes(graph['Zerind'], graph['Arad'], 75)
connectNodes(graph['Arad'], graph['Timisoara'], 118)
connectNodes(graph['Timisoara'], graph['Lugoj'], 111)
connectNodes(graph['Lugoj'], graph['Mehadia'], 70)
connectNodes(graph['Mehadia'], graph['Dobreta'], 75)
connectNodes(graph['Dobreta'], graph['Craiova'], 120)
connectNodes(graph['Sibiu'], graph['Oradea'], 151)
connectNodes(graph['Sibiu'], graph['Arad'], 140)
connectNodes(graph['Sibiu'], graph['Fagaras'], 99)
connectNodes(graph['Sibiu'], graph['Rimnicu Vilcea'], 80)
connectNodes(graph['Rimnicu Vilcea'], graph['Pitesti'], 97)
connectNodes(graph['Rimnicu Vilcea'], graph['Craiova'], 146)
connectNodes(graph['Fagaras'], graph['Bucharest'], 211)
connectNodes(graph['Pitesti'], graph['Bucharest'], 101)
connectNodes(graph['Pitesti'], graph['Craiova'], 138)
connectNodes(graph['Bucharest'], graph['Giurgiu'], 90)
connectNodes(graph['Neamt'], graph['Iasi'], 87)
connectNodes(graph['Iasi'], graph['Urziceni'], 142)
connectNodes(graph['Urziceni'], graph['Bucharest'], 85)
connectNodes(graph['Urziceni'], graph['Hirsova'], 98)
connectNodes(graph['Hirsova'], graph['Eforie'], 86)


