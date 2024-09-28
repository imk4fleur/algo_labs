import resource
import time

def main():
    # Starting time measuring
    start_time = time.perf_counter()

    # Reading from the input file
    with open("input.txt") as f:
        n = int(f.readline())
        a = list(map(int, f.readline().split()))
        b = list(map(int, f.readline().split()))

    a.sort()
    b.sort()

    answer = 0
    for i in range(n):
        answer += a[i] * b[i]

    # Writing to the output file
    with open("output.txt", "w") as f:
        f.write(str(answer))

    # Writing the time measurements to the standard output
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"Execution time: {duration}s")

    # Writing memory usage to the standard output
    memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(f"Memory usage: {memory_usage}B")

if __name__ == "__main__":
    main()