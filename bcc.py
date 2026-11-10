from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BCCUtil(self, u, parent, low, disc, stack):
        children = 0
        disc[u] = low[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if disc[v] == -1:
                parent[v] = u
                stack.append((u, v))
                children += 1
                self.BCCUtil(v, parent, low, disc, stack)

                low[u] = min(low[u], low[v])

                if low[v] >= disc[u]:
                    print("Bi-connected component:", end=" ")
                    while stack[-1] != (u, v):
                        print(stack.pop(), end=" ")
                    print(stack.pop())
            elif v != parent[u] and low[u] > disc[v]:
                low[u] = disc[v]
                stack.append((u, v))

    def BCC(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        parent = [-1] * self.V
        stack = []

        for i in range(self.V):
            if disc[i] == -1:
                self.BCCUtil(i, parent, low, disc, stack)

# --------- MAIN PROGRAM ----------
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

g = Graph(V)

print("Enter edges (u v):")
for _ in range(E):
    u, v = map(int, input().split())
    g.add_edge(u, v)

print("\nBi-connected components are:")
g.BCC()

