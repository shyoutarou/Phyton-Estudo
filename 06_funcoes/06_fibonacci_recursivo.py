def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


for n in range(10):
    print(fibonacci(n))
