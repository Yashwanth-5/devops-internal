#Bellman-Ford Algorithm

V, E = map(int, input("Enter number of vertices and edges: ").split())
edges = []
print("Enter edges (u v w):")
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

src = int(input("Enter source vertex: "))
dist = [float('inf')] * V
dist[src] = 0
for _ in range(V - 1):
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[v] > dist[u] + w:
            dist[v] = dist[u] + w

for u, v, w in edges:
    if dist[u] != float('inf') and dist[v] > dist[u] + w:
        print("\nGraph contains a negative weight cycle!")
        break
else:
    print("\nShortest distances from source vertex", src, ":")
    for i in range(V):
        print(f"{src} -> {i} = {dist[i]}")
