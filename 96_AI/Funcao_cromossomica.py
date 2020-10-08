import numpy as np

x = np.arange(2.31, -1.89)
f = np.exp(-2.3054)
print(f) # 0.09971890511299725
pe = 1 / (1 + f)
print(pe) # 0.9093232782946921

f = np.exp(1.8936)
print(f) # 6.643241353322455
pe = 1 / (1 + f)
print(pe) # 0.13083454437367834
