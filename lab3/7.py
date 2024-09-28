from collections import deque

total_colors = []
slides = []
sides = {}

def half_graph(u):
    global sides, total_colors
    search_queue = deque()
    search_queue.append((u, 0))
    visited = []
    while search_queue:
        cur_node, color = search_queue.popleft()
        if cur_node not in visited:
            total_colors[cur_node] = color
            visited.append(cur_node)
            for node in sides[cur_node]:
                if color == 0:
                    search_queue.append((node, 1))
                else:
                    search_queue.append((node, 0))
        elif total_colors[cur_node] != color:
            return 0
    return 1

def main():
    global slides
    global sides

    f = open('input.txt')
    n, m = map(int, f.readline().split())
    sides = {}
    for i in range(n+1):
        sides[i] = []
    for i in range(m):
        v1, v2 = map(int, f.readline().split())
        sides[v1].append(v2)
        sides[v2].append(v1)

    global total_colors

    total_colors = [None] * (n+1)

    with open('output.txt', 'w') as f:
        f.write(str(half_graph(1)))

if __name__ == "__main__":
    main()