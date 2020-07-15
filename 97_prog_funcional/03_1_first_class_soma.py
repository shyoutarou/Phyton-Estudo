def soma(x, y): return x + y

#<class 'function'>
print(type(soma))

s = soma
print(s(1, 2)) # 3
print(soma(1, 2)) # 3


def caller(f):
    return f()

def say_hello():
    return "Hello {0}".format("Baby")

print(caller(say_hello)) # Hello Baby