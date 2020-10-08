# Python3 program to implement traveling salesman
# problem using naive approach.
from sys import maxsize

V = 4


# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
            print(i)

            # store minimum weight Hamiltonian Cycle
    min_path = maxsize

    while True:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        tot_itens = len(vertex)
        otherSequence = range(tot_itens)
        print("Cont itens: " + str(tot_itens))
        soma = "0"
        for i in otherSequence:
            current_pathweight += graph[k][vertex[i]]
            soma = soma + " + " +  "graph[" + str(k)  + "][" + str(vertex[i])  + "](" + str(graph[k][vertex[i]])  + ")"
            k = vertex[i]

        current_pathweight += graph[k][s]
        soma = soma + " + " +  "graph[" + str(k)  + "][" + str(s)  + "](" + str(graph[k][s]) + ")"
        print("soma: " + soma)

        # update minimum
        min_path = min(min_path, current_pathweight)
        print(min_path)

        if not next_permutation(vertex):
            break

    return min_path


# next_permutation implementation
def next_permutation(L):
    n = len(L)

    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1

    L[i], L[j] = L[j], L[i]
    print("L[i]: " + str(L[i]))
    print("L[j]: " + str(L[j]))

    left = i + 1
    right = n - 1

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return True


# Driver Code
if __name__ == "__main__":
    # matrix representation of graph
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],
             [15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0
    print(travellingSalesmanProblem(graph, s))