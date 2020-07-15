def factorial(n):
    if n == 1:
        print(n)
        return 1
    else:
# 14 * 13 * 12 * 11 * 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
        print(n, '*', end=' ')
        return n * factorial(n - 1)

# 87178291200
print(factorial(14))
