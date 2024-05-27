from graph import graph

class DepthLimitedSearch:
    def __init__(self, start_city, goal_city, limit):
        self.start_city = start_city.name
        self.goal_city = goal_city.name
        self.limit = limit

    def search(self):
        node_stack = [(self.start_city, [self.start_city])]  # Tupla (cidade, caminho)
        explored = set()

        while node_stack:
            current_city, path = node_stack.pop()
            if current_city == self.goal_city:
                print("Path:", " -> ".join(path))
                return path

            if len(path) <= self.limit:
                if current_city not in explored:
                    explored.add(current_city)
                    for connection in graph[current_city].conections:
                        new_city = connection['node'].name
                        new_path = path + [new_city]
                        node_stack.append((new_city, new_path))

        print("Goal city not found within depth limit")
        return None




nome_origem = input("Digite a cidade de origem: ")
nome_destino = input("Digite a cidade de destino: ")

start_city = graph[nome_origem]
goal_city = graph[nome_destino]

DepthLimitedSearch(start_city, goal_city, 1).search()

