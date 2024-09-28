def run():
    with open("input.txt") as fin:
        host_line = fin.readline().split()
        n, A = int(host_line[0]), float(host_line[1])
        result, error = 10 ** 9, 0.1 ** 10
        heights = [0] * n
        heights[0] = A
        left, right = 0, heights[0]

        while abs(right - left) > error:
            heights[1] = (left + right) / 2
            heights[-1] = 0
            is_up = False

            for i in range(2, n):
                heights[i] = 2 * heights[i - 1] - heights[i - 2] + 2
                if heights[i] <= error:
                    is_up = True
                    break

            if heights[-1] > error:
                result = min(result, heights[-1])
            if is_up:
                left = heights[1]
            else:
                right = heights[1]

        return result


def main():
    with open("output.txt", "w") as fout:
        print("%.6f" % run(), file=fout)

if __name__ == "__main__":
    main()
