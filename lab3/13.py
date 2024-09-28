def main():
    f = open('input.txt')
    arr = []
    n, m = map(int, f.readline().split())
    for i in range(n):
        arr.append(f.readline()[:m])

    visited = [[False for _ in range(m)] for _ in range(n)]

    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                if arr[i][j] == '#':
                    count += 1
                    stack = [(i, j)]
                    while len(stack) != 0:
                        x, y = stack.pop()
                        if arr[x][y] == '#' and not visited[x][y]:
                            visited[x][y] = True
                            if x != 0:
                                stack.append((x-1, y))
                            if x != n-1:
                                stack.append((x+1, y))
                            if y != 0:
                                stack.append((x, y-1))
                            if y != m-1:
                                stack.append((x, y+1))

    d = open('output.txt', 'w')
    d.write(str(count))

if __name__ == "__main__":
    main()