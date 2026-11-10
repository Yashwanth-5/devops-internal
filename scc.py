from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Step 1: DFS and push vertices by finish time
    def dfs(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, stack)
        stack.append(v)

    # Step 2: Transpose graph
    def transpose(self):
        g = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                g.add_edge(v, u)
        return g

    # Step 3: DFS on transposed graph
    def dfs_util(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited, component)

    # Main SCC function
    def SCC(self):
        stack = []
        visited = [False] * self.V

        # First DFS
        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)

        # Transpose graph
        gr = self.transpose()
        visited = [False] * self.V

        print("\nStrongly Connected Components are:")
        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                gr.dfs_util(v, visited, component)
                print(component)
# --------- MAIN PROGRAM ----------
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

g = Graph(V)

print("Enter directed edges (u v):")
for _ in range(E):
    u, v = map(int, input().split())
    g.add_edge(u, v)

g.SCC()

