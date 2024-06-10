from graph import graph

def bfs_shortest_path(graph, start_node, end_node):
    visited = []  # Lista para armazenar nós visitados
    queue = [(start_node, [start_node])]  # Inicializa a fila com o nó inicial e o caminho até ele
    
    while queue:
        node, path = queue.pop(0)  # Remove o primeiro elemento da fila
        if node == end_node:
            return path  # Retorna o caminho quando o destino é encontrado
        if node not in visited:
            visited.append(node)  # Adiciona o nó à lista de visitados
            
            # Adiciona todos os vizinhos não visitados à fila com seus respectivos caminhos
            for connection in node.conections:
                neighbor = connection['node']
                if neighbor not in visited:
                    new_path = path + [neighbor]  # Adiciona o vizinho ao caminho
                    queue.append((neighbor, new_path))

nome_origem = input("Digite a cidade de origem: ")
nome_destino = input("Digite a cidade de destino: ")

origem = graph[nome_origem]
destino = graph[nome_destino]
caminho = bfs_shortest_path(graph, origem, destino)
print("Caminho mais curto de", origem.name, "para", destino.name, ":", [cidade.name for cidade in caminho])

