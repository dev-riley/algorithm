n = input()
str = ''
for i in n:
    if ord(i) - 3 > 90:
        str += chr(ord(i) - 26 - 3)
    elif ord(i) - 3 < 65:
        str += chr(ord(i) + 26 - 3)
    else:
        str += chr(ord(i) - 3)
print(str)