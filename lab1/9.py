import resource
import time

def main():
    # Starting time measuring
    start_time = time.perf_counter()

    p = {}

    # Reading from the input file
    with open("input.txt") as f:
        n = int(f.readline())
        for i in range(7):
            p[10 ** i] = int(f.readline())

    dp = []
    dp.append(0)

    for i in range(1, max(n + 1, 10 ** 6 + 1)):
        dp.append(p[1] * i)
        for j in p:
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + p[j])

    ans = dp[n]
    for i in range(n + 1, 10 ** 6 + 1):
        ans = min(ans, dp[i])

    # Writing to the output file
    with open("output.txt", "w") as f:
        f.write(str(ans) + "\n")

    # Writing the time measurements to the standard output
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"Execution time: {duration}s")

    # Writing memory usage to the standard output
    memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(f"Memory usage: {memory_usage}B")

if __name__ == "__main__":
    main()