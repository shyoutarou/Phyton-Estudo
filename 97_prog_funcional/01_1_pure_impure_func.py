# Create a global variable `A`.
A = 5

def impure_sum(b):
    # Adds two numbers, but uses the
    # global `A` variable.
    return b + A

def pure_sum(a, b):
    # Adds two numbers, using
    # ONLY the local function inputs.
    return a + b

print(impure_sum(5)) # 10
print(pure_sum(4, 6)) # 10

# Abordagem tradicional Imperativo
prices = [50, 60, 70]
newPrices = []
for price in prices:
    newPrice = price * 1.1
    newPrices.append(newPrice)
print (newPrices) # [55.00000000000001, 66.0, 77.0]

# Função pura Funcional
prices = [50, 60, 70]
list(map(lambda price: price * 1.1 , prices))
print (prices) # [50, 60, 70]


