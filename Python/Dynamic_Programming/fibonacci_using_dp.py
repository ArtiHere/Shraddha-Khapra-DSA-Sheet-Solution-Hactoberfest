def fibonacci(n):
    if n <= 1:
        return n

    # Create a table to store previously computed Fibonacci numbers
    fib_table = [0] * (n + 1)
    fib_table[1] = 1

    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]

    return fib_table[n]

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    result = fibonacci(n)
    print(f"The {n}-th Fibonacci number is {result}.")
