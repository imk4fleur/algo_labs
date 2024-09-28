from collections import deque

sides = {}

def short_path(u, v):
    global sides
    search_queue = deque()
    search_queue.append((u, 0))
    visited = []
    while search_queue:
        cur_node, path = search_queue.popleft()
        if cur_node == v:
            return path
        path += 1
        if cur_node not in visited:
            visited.append(cur_node)
            if cur_node in sides:
                for node in sides[cur_node]:
                    search_queue.append((node, path))
    return -1

def main():
    f = open('input.txt')
    m = int(f.readline())
    global sides
    for i in range(m):
        v1, sigh, v2 = map(str, f.readline().split())
        if v1 in sides:
            sides[v1].append(v2)
        else:
            sides[v1] = [v2]
    u = f.readline()[:-1]
    v = f.readline()[:-1]

    result = short_path(u, v)

    d = open('output.txt', 'w')
    d.write(str(result))

if __name__ == "__main__":
    main()