#Dijkstras
import heapq
V, E = map(int, input("Enter number of vertices and edges: ").split())
adj = [[] for _ in range(V)]

directed = input("Is the graph directed? (y/n): ").lower() == 'y'

print("Enter edges (u v w):")
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    if not directed:
        adj[v].append((u, w))

src = int(input("Enter source vertex: "))

dist = [float('inf')] * V
dist[src] = 0
pq = [(0, src)]

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in adj[u]:
        if dist[v] > d + w:
            dist[v] = d + w
            heapq.heappush(pq, (dist[v], v))

print("\nShortest distances from source vertex", src, ":")
for i in range(V):
    print(f"{src} -> {i} = {dist[i]}")
