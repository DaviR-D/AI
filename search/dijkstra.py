from graph import graph

def dijkstra_shortest_path(graph, start_node, end_node):
    # Dicionário para armazenar as distâncias dos nós à origem
    distances = {node.name: float('inf') for node in graph.values()}
    distances[start_node.name] = 0  # Define a distância da origem para ela mesma como 0
    
    # Dicionário para armazenar os predecessores de cada nó no caminho mais curto
    predecessors = {node.name: None for node in graph.values()}
    
    # Lista para armazenar nós visitados
    visited = []
    
    # Encontra o nó mais próximo ainda não visitado
    def closest_node():
        min_distance = float('inf')
        closest_node = None
        for node in graph.values():
            if distances[node.name] < min_distance and node.name not in visited:
                min_distance = distances[node.name]
                closest_node = node
        return closest_node
    
    # Loop principal
    while True:
        closest = closest_node()  # Encontra o nó mais próximo ainda não visitado
        if closest is None:
            break  # Se todos os nós foram visitados, sai do loop
        
        visited.append(closest.name)  # Marca o nó como visitado
        
        # Atualiza as distâncias e os predecessores dos vizinhos do nó mais próximo
        for connection in closest.conections:
            neighbor = connection['node']
            weight = connection['weight']
            if distances[closest.name] + weight < distances[neighbor.name]:
                distances[neighbor.name] = distances[closest.name] + weight
                predecessors[neighbor.name] = closest.name
    
    # Constrói o caminho a partir dos predecessores
    path = []
    current_node = end_node.name
    while current_node is not None:
        path.insert(0, current_node)
        current_node = predecessors[current_node]
        if current_node is not None and current_node == start_node.name:
            path.insert(0, current_node)
            break
    
    if path[0] == path[1]:
        return None
    
    return [graph[node] for node in path]

nome_origem = input("Digite a cidade de origem: ")
nome_destino = input("Digite a cidade de destino: ")

origem = graph[nome_origem]
destino = graph[nome_destino]
caminho = dijkstra_shortest_path(graph, origem, destino)
print("Caminho mais curto de", origem.name, "para", destino.name, ":", [cidade.name for cidade in caminho])
