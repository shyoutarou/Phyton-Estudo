def hello():
    print("Ola Mundo!!!")


# Para usar a função, basta chama-la pelo nome:
hello()


def maior(x, y):
    if x > y:
        print("0 valor " + str(x) + " é maior do que " + str(y))
    else:
        print("0 valor " + str(y) + " é maior do que " + str(x))

maior(5, 1) # 0 valor 5 é maior do que 1

import pandas as pd


matrix = [[5, 6],
            [1, 7, 9],
            [3, 2]]
print(matrix)
df_scaler = pd.DataFrame(data=matrix)
print(df_scaler)
print(df_scaler.index)
print(len(df_scaler.index))

vector_y = [[5, 6, 1]]
print(vector_y)
print(len(vector_y))

def perc_set(m, d):
    return ((len(m)/len(d.index)) * 100)

porcentagem = perc_set(vector_y, df_scaler)
print(porcentagem)