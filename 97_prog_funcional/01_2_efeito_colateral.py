def read_and_print(filename):
    with open(filename, 'r', encoding="utf8") as f:
        # Side effect of opening a
        # file outside of function.
        data = [line for line in f]
    for line in data:
        # Call out to the operating system
        # "println" method (side effect).
        print(line)

read_and_print('nome_errado.txt')

