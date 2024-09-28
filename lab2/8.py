def main():
    with open("input.txt") as fin:
        n = int(fin.readline())
        woods = []
        deeps = [0] * (n + 1)

        for _ in range(n):
            value, left, right = map(int, fin.readline().split())
            woods.append((left, right))

        for i in range(n - 1, -1, -1):
            if (woods[i][0] == 0) and (woods[i][1] == 0):
                deeps[i + 1] = 1
            else:
                deeps[i + 1] = max(deeps[woods[i][0]], deeps[woods[i][1]]) + 1

    with open("output.txt", "w") as fout:
        if n > 0:
            print(deeps[1], file=fout)
        else:
            fout.write("0")

if __name__ == "__main__":
    main()