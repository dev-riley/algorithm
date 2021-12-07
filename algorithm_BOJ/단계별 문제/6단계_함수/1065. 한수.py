N = int(input())
num = 0
for i in range(1, N + 1):
    if i < 100:
        num += 1
    else:
        if i % 10 - (i // 10) % 10 == (i // 10) % 10 - i // 100:
            num += 1
print(num)