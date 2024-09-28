def maze(graph, visited, node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            maze(graph, visited, neighbor)


def components(graph, n):
    visited = [False] * n
    count = 0
    for vertex in range(n):
        if not visited[vertex]:
            count += 1
            maze(graph, visited, vertex)
    return count

def main():
    with open('input.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

    with open('output.txt', 'w') as f:
        f.write(str(components(graph, n)))

if __name__ == "__main__":
    main()