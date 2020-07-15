# Higher Order Functions — Closure
def add_x(x):
    def adder(y):
        return x + y
    return adder

add_5 = add_x(5)
add_7 = add_x(7)
print(add_5(10)) # result 15
print(add_7(10)) # result 17


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)

# <function make_multiplier_of.<locals>.multiplier at 0x0000020A4CAA6CA8>
print(times3)
print(times3.__closure__[0].cell_contents) # 3

print(times3(9)) # Output: 27
print(times5(3)) # Output: 15
print(times5(times3(2))) # Output: 30