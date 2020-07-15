def fibonacci(n, first: int = 0, second: int = 1):
    for _ in range(n):
        yield first
        first, second = second, first + second  # Assignment
print(list(fibonacci(10)))