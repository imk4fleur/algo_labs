import resource
import time


# Starting time measuring
start_time = time.perf_counter()

# Performs an arithmetic operation between two numbers a and b
def eval(a, b, op):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b

# Function to calculate the minimum and maximum values ​​for a subexpression
def min_and_max(i, j, min_array, max_array, operators):
    min_value = float('inf')
    max_value = float('-inf')

    # Iterate over all possible operators between i and j
    for k in range(i, j):
        op = operators[k]
        a = eval(min_array[i][k], min_array[k + 1][j], op)
        b = eval(min_array[i][k], max_array[k + 1][j], op)
        c = eval(max_array[i][k], min_array[k + 1][j], op)
        d = eval(max_array[i][k], max_array[k + 1][j], op)

        # Update minimum and maximum values
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)

    return min_value, max_value

# Returns the maximum possible value of an expression
def get_maximum_value(expression):

    digits = []
    operators = []

    # Separation of numbers and operators
    for i, c in enumerate(expression):
        if i % 2 == 0:
            digits.append(int(c))
        else:
            operators.append(c)

    n = len(digits)

    # Initializing tables for minimum and maximum values
    min_array = [[0] * n for _ in range(n)]
    max_array = [[0] * n for _ in range(n)]

    # Filling the diagonal of the table with the original numbers
    for i in range(n):
        min_array[i][i] = digits[i]
        max_array[i][i] = digits[i]

    # Loop by subexpression size
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            min_array[i][j], max_array[i][j] = min_and_max(i, j, min_array, max_array, operators)

    # Return the maximum value for the entire expression
    return max_array[0][n - 1]

def main():
    # Reading data from input.txt file
    with open('input.txt', 'r') as f:
        expression = f.readline().strip()

    # Finding the maximum value of an expression
    result = get_maximum_value(expression)

    # Write the result to the output.txt file
    with open('output.txt', 'w') as f:
        f.write(str(result))

    # Writing the time measurements to the standard output
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"Execution time: {duration}s")

    # Writing memory usage to the standard output
    memory_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(f"Memory usage: {memory_usage}B")

if __name__ == "__main__":
    main()