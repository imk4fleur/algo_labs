import resource
import time


def main():
    # Starting time measuring
    start_time = time.perf_counter()

    # Reading from the input file
    with open("input.txt", "r") as f:
        n = int(f.readline())
        costs = []
        for i in range(n):
            costs.append(int(f.readline()))

    # Сreating dp to store minimum values
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    # Filling dp
    for i in range(1, n + 1):
        for j in range(n + 1):
            if j < n:
                dp[i][j] = dp[i - 1][j + 1]

            if costs[i - 1] > 100:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + costs[i - 1])
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + costs[i - 1])

    # Finding the minimum cost and the number of unused coupons
    min_cost = float('inf')
    for j in range(n + 1):
        if dp[n][j] <= min_cost:
            min_cost = dp[n][j]
            unused_coupons = j

    # Recovering path and finding days of using coupons
    days = []
    i, j = n, unused_coupons
    while i > 0:
        if dp[i][j] == dp[i - 1][j + 1]:
            days.append(i)
            j += 1
        elif costs[i - 1] > 100 and dp[i][j] == dp[i - 1][j - 1] + costs[i - 1]:
            j -= 1
        i -= 1
    days.reverse()

    # Write the result to the output.txt file
    with open('output.txt', 'w') as f:
        f.write(str(min_cost) + "\n")
        f.write(str(unused_coupons) + " " + str(len(days)) + "\n")
        for day in days:
            f.write(str(day) + "\n")

    # Writing the time measurements to the standard output
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"Execution time: {duration}s")

    # Writing memory usage to the standard output
    memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(f"Memory usage: {memory_usage}B")

if __name__ == "__main__":
    main()