import resource
import time

def main():
    # Starting time measuring
    start_time = time.perf_counter()

    # Reading from the input file
    with open("input.txt") as f:
        n = int(f.readline())

    cur_candies = 0
    all_candies = []
    for k in range(1, n + 1):
        if cur_candies + k <= n:
            all_candies.append(k)
            cur_candies += k
            answer = k
        else:
            all_candies[-1] += n - cur_candies
            break

    # Writing to the output file
    with open("output.txt", "w") as f:
        f.write(str(answer) + "\n")
        f.write(" ".join(list(map(str, all_candies))))

    # Writing the time measurements to the standard output
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"Execution time: {duration}s")

    # Writing memory usage to the standard output
    memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(f"Memory usage: {memory_usage}B")

if __name__ == "__main__":
    main()