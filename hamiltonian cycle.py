#Hamiltonian-Cycle
def is_safe(v, graph, path, pos):
    if graph[path[pos-1]][v] == 0:
        return False
    if v in path:
        return False
    return True
def hamiltonian_cycle_util(graph, path, pos):
    if pos == len(graph):
        if graph[path[pos-1]][path[0]] == 1:
            return True
        else:
            return False
    for v in range(1, len(graph)):
        if is_safe(v, graph, path, pos):
            path[pos] = v
            if hamiltonian_cycle_util(graph, path, pos+1):
                return True
            path[pos] = -1
    return False
def find_hamiltonian_cycle(graph):
    path = [-1] * len(graph)
    path[0] = 0
    if hamiltonian_cycle_util(graph, path, 1):
        path.append(path[0])
        return path
    else:
        return None
def main():
    V = int(input("Enter number of vertices: "))
    print("Enter adjacency matrix row-wise (space separated):")
    graph = [list(map(int, input().split())) for _ in range(V)]
    cycle = find_hamiltonian_cycle(graph)
    if cycle:
        print("Hamiltonian Cycle found:")
        print(" -> ".join(map(str, cycle)))
    else:
        print("No Hamiltonian Cycle exists")
if __name__ == "__main__":
    main()
