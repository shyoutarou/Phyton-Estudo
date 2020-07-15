print(ord('B'))
print(ord('C'))
print(ord('Z'))

print(chr(65))
print(chr(98))
print(chr(43))

normalText = 'Python is interesting'
print(ascii(normalText))

otherText = 'Pythön is interesting'
print(ascii(otherText))

print('Pyth\xf6n is interesting')

for i in range(1, 255):
    ch = chr(i)
    ordem = ord(ch)
    print(i, "=", ch)
    print(ch, "=", ordem)

