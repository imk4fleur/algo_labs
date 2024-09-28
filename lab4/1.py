def main():
    with open('input.txt') as f:
        p = f.readline()[:-1]
        t = f.readline()

    count = 0
    res = ''
    for i in range(len(t) - len(p) + 1):
        if t[i] == p[0]:
            part = t[i:i+len(p)]
            if part == p:
                count += 1
                res += str(i+1) + ' '
    res = res[:-1]

    with open('output.txt', 'w') as f:
        f.write(str(count) + '\n' + str(res))

if __name__ == '__main__':
    main()