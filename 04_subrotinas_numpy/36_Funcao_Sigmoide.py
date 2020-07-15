import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

print(sigmoid(1.10)) # 0.7502601055951177
print(sigmoid(1.00)) # 0.7310585786300049
print(sigmoid(0.90)) # 0.7109495026250039
print(sigmoid(0.70)) # 0.6681877721681662
print(sigmoid(0.50)) # 0.6224593312018546

print(sigmoid(2.31)) # 0.9097018552970803
print(sigmoid(-1.89)) # 0.13124446943852333