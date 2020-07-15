# Continue >> Uma variação do if else, mais enxuta:
num = int(input("Digite um numero inteiro: "))
d = 2
while num > 1:
    if num % d == 0:
        print(d)
        num = num / d
        continue
    d = d + 1

print("====================")

num = 0
while num < 5:
    num = num + 1
    if num == 3:
        continue
    print("Num =  {} ".format(num))
print("Out of loop")

print("====================")

num = 0
while num < 5:
    num = num + 1
    if num != 3:
        print("Num =  {} ".format(num))
print("Out of loop")

print("====================")

num = 0
while num < 5:
    num = num + 1
    if num == 3:
        pass
        continue
    print("Num =  {} ".format(num))
print("Out of loop")

print("====================")

num = int(input("enter a number"))
d = 2
while num > 1:
    print(d)
    print(num)
    print("if " + str(num % d == 0))
    if num % d == 0:
        print(d)
        print(num)
        num = num / d
        print(num)
        print("===")
        continue
    print(str(d + 1) + "=" + str(d) + "+1")
    d = d + 1
    print("===")

print("====================")

num = int(input("enter a number"))
d = 2
while num > 1:
    print(d)
    print(num)
    print("if " + str(num % d == 0))
    if num % d == 0:
        print(d)
        print(num)
        num = num / d
        print(num)
        print("===")
    else:
        print(str(d + 1) + "=" + str(d) + "+1")
        d = d + 1
        print("===")


