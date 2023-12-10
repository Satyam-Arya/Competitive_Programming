from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True

        for neighbor in self.adj_list[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, v):
                    return True
            elif parent != neighbor:
                return True

        return False

    def contains_cycle(self):
        visited = [False] * self.vertices

        for i in range(self.vertices):
            if not visited[i]:
                if self.is_cyclic_util(i, visited, -1):
                    return 1  # Cycle is detected

        return 0  # No cycle is detected

if __name__ == "__main__":
    # Construct a sample graph
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(1, 3)

    result = g.contains_cycle()
    print("Does the graph contain a cycle?", result)
