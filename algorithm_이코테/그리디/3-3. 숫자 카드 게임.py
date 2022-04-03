N,M = map(int,input().split())

res = 0
for i in range(N):
    data = list(map(int, input().split()))
    min_value = 10001
    for j in data:
        if j < min_value:
            min_value = j
    res = max(res, min_value)
print(res)