import resource
import time

def main():
    # Starting time measuring
    start_time = time.perf_counter()

    MOD = 10 ** 9

    # Reading from the input file
    with open("input.txt") as f:
        n = int(f.readline())

    dp = [[0] * 10 for _ in range(n + 1)]
    for i in range(10):
        dp[1][i] = 1

    for i in range(2, n + 1):
        dp[i][0] = (dp[i - 1][4] + dp[i - 1][6]) % MOD
        dp[i][1] = (dp[i - 1][6] + dp[i - 1][8]) % MOD
        dp[i][2] = (dp[i - 1][7] + dp[i - 1][9]) % MOD
        dp[i][3] = (dp[i - 1][4] + dp[i - 1][8]) % MOD
        dp[i][4] = (dp[i - 1][0] + dp[i - 1][3] + dp[i - 1][9]) % MOD
        dp[i][6] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][7]) % MOD
        dp[i][7] = (dp[i - 1][2] + dp[i - 1][6]) % MOD
        dp[i][8] = (dp[i - 1][1] + dp[i - 1][3]) % MOD
        dp[i][9] = (dp[i - 1][2] + dp[i - 1][4]) % MOD

    ans = 0
    for i in range(10):
        ans += dp[n][i]
    ans -= dp[n][0] + dp[n][8]

    # Write the result to the output.txt file
    with open('output.txt', 'w') as f:
        f.write(str(ans))

    # Writing the time measurements to the standard output
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"Execution time: {duration}s")

    # Writing memory usage to the standard output
    memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(f"Memory usage: {memory_usage}B")

if __name__ == "__main__":
    main()