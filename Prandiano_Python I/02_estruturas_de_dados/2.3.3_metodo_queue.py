"""
Esta forma de carregar um pacote, na verdade, faz com que se carregue
apenas uma parte, neste caso, a função deque
"""
from collections import deque

# Tentar exeutar o mesmo código sem o deque
# matematicos = ["Euler", "John Napier", "Michael Stiefel"] # <class 'list'>
# <class 'collections.deque'>
matematicos = deque(["Euler", "John Napier", "Michael Stiefel"])
print(type(matematicos))

matematicos.append("Torricelli")
print(matematicos)

matematicos.append("Grasman")
print(matematicos)

# Erro sem o deque: AttributeError: 'list' object has no attribute 'popleft'
matematicos.popleft()
print(matematicos)

matematicos.popleft()
print(matematicos)
