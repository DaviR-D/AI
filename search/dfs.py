from graph import graph

class DepthLimitedSearch:
    def __init__(self, start_city, goal_city):
        self.start_city = start_city.name
        self.goal_city = goal_city.name

    def search(self):
        node_stack = [(self.start_city, [self.start_city])]  # Tupla (cidade, caminho)
        explored = set()

        while node_stack:
            current_city, path = node_stack.pop()
            if current_city == self.goal_city:
                print("Goal city found")
                return path

            if current_city not in explored:
                explored.add(current_city)
                for connection in graph[current_city].conections:
                    new_city = connection['node'].name
                    new_path = path + [new_city]
                    node_stack.append((new_city, new_path))

        print("Goal city not found")
        return None


start_city = graph['Oradea']
goal_city = graph['Eforie']

path = DepthLimitedSearch(start_city, goal_city).search()
if path:
    print("Path:", " -> ".join(path))
else:
    print("No path found.")
