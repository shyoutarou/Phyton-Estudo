values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map.
add_10 = list(map(lambda x: x + 10, values))
print(add_10)

# Filter.
even = list(filter(lambda x: x % 2 == 0, values))
print(even)

# Com list comprehensions
add_10 = [x + 10 for x in values]
print(add_10) # [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

even = [x for x in values if x % 2 == 0]
print(even) # [2, 4, 6, 8, 10]