n = int(input())
range_data = []
for _ in range(n):
    data = list(map(int, input().split()))
    range_data.append(data)

ans = 0
q = int(input())
for i in range(q):
    x, y = map(int, input().split())
    for j in range_data:
        print(j)
        if x >= j[0] and y <= j[1]:
            ans += 1
        else:
            continue

    if ans != 0:
        print(ans)
    else:
        print(-1)