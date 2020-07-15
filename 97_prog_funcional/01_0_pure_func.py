# Python program to demonstrate pure functions

# A pure function that does Not changes
# the input list and returns the new List
def pure_func(List):
    New_List = []
    for i in List:
        New_List.append(i ** 2)
    return New_List

Original_List = [1, 2, 3, 4]
Modified_List = pure_func(Original_List)

# Original List: [1, 2, 3, 4]
print("Original List:", Original_List)
# Modified List: [1, 4, 9, 16]
print("Modified List:", Modified_List) 


valor = 5

def mais_cinco(x):
    return x + valor

assert mais_cinco(5) == 10 # True
valor = 7
assert mais_cinco(5) == 10 # AssertionError