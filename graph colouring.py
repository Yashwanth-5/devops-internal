#Implement graph coloring problem using backtracking
def isSafe(v, graph, color, c):
    return all(graph[v][i] == 0 or color[i] != c for i in range(len(graph)))

def solve(graph, m, color, v=0):
    if v == len(graph): return True
    for c in range(1, m+1):
        if isSafe(v, graph, color, c):
            color[v] = c
            if solve(graph, m, color, v+1): return True
            color[v] = 0
    return False

n = int(input("Enter number of vertices: "))
graph = [list(map(int, input().split())) for _ in range(n)]
m = int(input("Enter number of colors: "))

color = [0]*n
if solve(graph, m, color): print(" Coloring:", color)
else: print(" No solution")
