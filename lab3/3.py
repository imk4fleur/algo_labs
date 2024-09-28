def solve():
    f = open('input.txt')
    n, m = map(int, f.readline().split())
    sides = {}
    for i in range(1, n+1):
        sides[i] = []
    for i in range(m):
        v1, v2 = map(int, f.readline().split())
        sides[v1].append(v2)

    for u in sides:
        visited = []
        parent = {}
        cur_node = u
        node_found = 1
        node_completed = 0
        while True:
            visited.append(cur_node)
            flag = False
            for i in sides[cur_node]:
                if i == u:
                    return 1
                if i not in visited:
                    parent[i] = cur_node
                    cur_node = i
                    node_found += 1
                    flag = True
                    break
            if not flag:
                node_completed += 1
                if node_found == node_completed:
                    break
                cur_node = parent[cur_node]
    return 0

def main():
    with open('output.txt', 'w') as f:
        f.write(str(solve()))

if __name__ == "__main__":
    main()