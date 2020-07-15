"""
Números Racionais.
Perceber que o erro a seguir é proposital.
A função Range só aceita números INTEIROS para o passo.
"""

import numpy as np

racionais = list(range(-10, 10, 0.05))
print(racionais)
print(type(racionais))
print("")

racionais = np.array(racionais)
print(racionais)
print(type(racionais))
