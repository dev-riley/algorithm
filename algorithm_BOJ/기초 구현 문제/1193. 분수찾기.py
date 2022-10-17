n = int(input())
i, num = 0, 0
while n > num:
    i += 1
    num += i

if i % 2 == 0:
    a = i - (num - n)
    b = (num - n) + 1
else:
    a = (num - n) + 1
    b = i - (num - n)
print(f'{a}/{b}')