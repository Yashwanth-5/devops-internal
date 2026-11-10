#Floyd–Warshall Algorithm
V, E = map(int, input("Enter number of vertices and edges: ").split())
INF = float('inf')
dist = [[INF] * V for _ in range(V)]
for i in range(V):
    dist[i][i] = 0

print("Enter edges (u v w):")
for _ in range(E):
    u, v, w = map(int, input().split())
    dist[u][v] = w
    dist[v][u] = w
for k in range(V):
    for i in range(V):
        for j in range(V):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

print("\nAll-pairs shortest distances:")
for i in range(V):
    for j in range(V):
        if dist[i][j] == INF:
            print("-1", end=" ")
        else:
            print(dist[i][j], end=" ")
    print()
