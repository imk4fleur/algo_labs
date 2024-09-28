def main():
    with open('input.txt', 'r') as f_in:
        s = f_in.readline()
        n = len(s)
        pi = [0] * n

    l, r = -1, -1
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j

    with open('output.txt', 'w') as f_out:
        f_out.write(' '.join(list(map(str, pi[:-1]))))

if __name__ == '__main__':
    main()