import resource
import time


def main():
    # Starting time measuring
    start_time = time.perf_counter()

    # Reading from the input file
    with open("input.txt", "r") as f:
        n, k = map(int, f.readline().split(" "))
        s = f.readline()

    ans = 0

    # Odd sized sub-words
    for c in range(n):
        ans += 1
        changes_required = 0
        for l in range(1, n):
            if c - l < 0 or c + l >= n:
                break
            if s[c - l] != s[c + l]:
                if changes_required != k:
                    ans += 1
                    changes_required += 1
                else:
                    break
            else:
                ans += 1

    # Even sized sub-words
    for c in range(n):
        changes_required = 0
        for l in range(1, n):
            left = c - l + 1
            right = c + l
            if left < 0 or right >= n:
                break
            if s[left] != s[right]:
                if changes_required != k:
                    ans += 1
                    changes_required += 1
                else:
                    break
            else:
                ans += 1

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