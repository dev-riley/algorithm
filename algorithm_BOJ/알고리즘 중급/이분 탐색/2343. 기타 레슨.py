n, m = map(int, input().split())
data = list(map(int, input().split()))

start, end = 0, 10000000000
ans = []

while start <= end:
    mid = (start + end) // 2
    total = 0
    cnt = 0
    for i in data:
        total += i
        if total >= mid:
            cnt += 1
            ans.append(total)
            total = 0
    if cnt >= m:
        print(ans)
        start = mid + 1
    else:
        end = mid - 1

print(ans)