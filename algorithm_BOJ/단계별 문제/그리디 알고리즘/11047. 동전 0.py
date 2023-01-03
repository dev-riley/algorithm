n, k = map(int, input().split())
data = [int(input()) for _ in range(n)]
data.sort(reverse=True)

cnt = 0
for i in data:
    if i <= k:
        cnt += k // i
        k = k % i

print(cnt)