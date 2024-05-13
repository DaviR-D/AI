class Node():
    def __init__(self, name):
        self.name = name
        self.conections = list()
        
    def addConection(self, node, weight):
        self.conections.append({'node': node, 'weight': weight})




