num = int(input('Enter a number: '))
assert num >= 0, "Somente números positivos"
print('You entered: ', num)
# Se digitar 100 >> You entered:  100
""" Se digitar menor que 0
File "22_assert.py", line 2, in <module>
assert num >= 0
AssertionError: Somente números positivos
"""

try:
    num = int(input('Enter a number: '))
    assert (num >= 0), "Somente números positivos"
    print('You entered: ', num)
except AssertionError as msg:
    print(msg)
