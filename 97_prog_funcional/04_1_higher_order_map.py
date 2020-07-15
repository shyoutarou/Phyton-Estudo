# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
results = map(addition, numbers)

# Does not Prints the value
# <map object at 0x000001F60F49D088>
print(results)

# For Printing value
for result in results:
    print(result, end=" ") # 2 4 6 8

# Versão resumida usando lambda
lst = [1, 2, 3, 4]
double_lst = list(map(lambda x: x * 2, lst))

# [2, 10, 8, 12, 16, 22, 6, 24]
print("")
print(double_lst) # [2, 4, 6, 8]
