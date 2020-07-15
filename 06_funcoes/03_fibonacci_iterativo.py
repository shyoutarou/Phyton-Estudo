def fibonacci(n, first: int = 0, second: int = 1) -> None:
    for _ in range(n):
        print(first)  # Side-effect
        first, second = second, first + second  # Assignment
print(fibonacci(10))