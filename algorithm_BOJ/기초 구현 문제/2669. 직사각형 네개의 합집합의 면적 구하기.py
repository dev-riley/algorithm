arr = []
for _ in range(4):
    x, y, a, b = map(int, input().split())
    for i in range(x, a):
        for j in range(y, b):
            arr.append((i, j))
print(len(set(arr)))